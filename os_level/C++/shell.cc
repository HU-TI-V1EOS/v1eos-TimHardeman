#include "shell.hh"

int main()
{ std::string input;

  std::string configure = "configureShell";
  const char* charconfigure = configure.c_str();

  int configureFile = syscall(SYS_open, charconfigure, O_RDONLY, 0755);

  std::string prompt = "";

  char byte[1];
  while(syscall(SYS_read, configureFile, byte, 1)){
	prompt += byte;
  }
  prompt.pop_back();

  while(true)
  { std::cout << prompt;                   // Print het prompt
    std::getline(std::cin, input);         // Lees een regel
    if (input == "new_file") new_file();   // Kies de functie
    else if (input == "ls") list();        //   op basis van
    else if (input == "src") src();        //   de invoer
    else if (input == "find") find();
    else if (input == "seek") seek();
    else if (input == "exit") return 0;
    else if (input == "quit") return 0;
    else if (input == "error") return 1;

    if (std::cin.eof()) return 0; } }      // EOF is een exit

void new_file(){
	std::string bestandnaam = "";

	std::cout << "Geef een bestandnaam: " << '\n';
	std::cin >> bestandnaam;
	std::cin.ignore(1, '\n');

	const char* charnaam = bestandnaam.c_str();

	syscall(SYS_creat, charnaam, 0755);
	int file = syscall(SYS_open, charnaam, O_WRONLY, 0755);

	std::cout << "Geef een tekst: " << '\n';

	std::string string = "";
	while(true){
		std::getline(std::cin, string);
		if (string == "<EOF>"){
			break;
		}

		string += '\n';

		const char* charstring = string.c_str();

		syscall(SYS_write, file, charstring, strlen(charstring));
	}
	syscall(SYS_close, file);
}

void list(){
	int pid = syscall(SYS_fork);

	if (pid == 0){
	const char* args[] = { "/bin/ls", "-la", NULL };

	syscall(SYS_execve, args[0], args, NULL);
	}
	else{
	syscall(SYS_wait4, pid, NULL, NULL, NULL);
	}
}

void find(){
	std::string string = "";
        std::cout << "Geef een string: ";
        std::cin >> string;
	std::cin.ignore(1, '\n');

	const char* charstring = string.c_str();

	int fd[2];
	syscall(SYS_pipe, &fd);

	int pid = syscall(SYS_fork);
	if (pid == 0){
		syscall(SYS_close, fd[0]);
		syscall(SYS_dup2, fd[1], 1);

		const char * args[] = { "/usr/bin/find", ".", NULL };
		syscall(SYS_execve, args[0], args, NULL);
	}
	else{
		int pid2 = syscall(SYS_fork);
		if ( pid2 == 0){

		syscall(SYS_close, fd[1]);
		syscall(SYS_dup2, fd[0], 0);

		const char * args[] = { "/bin/grep", charstring, NULL };
		syscall(SYS_execve, args[0], args, NULL);
		}
		else{
		syscall(SYS_close, fd[0]);
		syscall(SYS_close, fd[1]);

		syscall(SYS_wait4, pid, NULL, NULL, NULL);
		syscall(SYS_wait4, pid2, NULL, NULL, NULL);
		}
	}

}

void seek(){
	int pid = syscall(SYS_fork);
        if (pid == 0){
		std::string seek = "seek";
        	const char* charseek = seek.c_str();

		int fileseek = syscall(SYS_creat, charseek, 0755);
		int file = syscall(SYS_open, charseek, O_WRONLY, 0755);

		std::string x = "x";
                const char* charx = x.c_str();

		syscall(SYS_write, fileseek, charx, strlen(charx));
		syscall(SYS_lseek, fileseek, 5000000, SEEK_CUR);
                syscall(SYS_write, fileseek, charx, strlen(charx));

		syscall(SYS_close, fileseek);
		}
	else{
		int pid2 = syscall(SYS_fork);
	        if (pid2 == 0){
			std::string loop = "loop";
		        const char* charloop = loop.c_str();

			syscall(SYS_creat, charloop, 0755);
			int fileloop = syscall(SYS_open, charloop, O_WRONLY, 0755);

			std::string x = "x";
                	const char* charx = x.c_str();

			syscall(SYS_write, fileloop, charx, strlen(charx));
			for(int i = 0; i < 5000000; i++){
                                syscall(SYS_write, fileloop, "\0", 1);
                        }
			syscall(SYS_write, fileloop, charx, strlen(charx));

			syscall(SYS_close, fileloop);
		}
		else{
			syscall(SYS_wait4, pid, NULL, NULL, NULL);
			syscall(SYS_wait4, pid2, NULL, NULL, NULL);
		}
	}
}

void src() // Voorbeeld: Gebruikt SYS_open en SYS_read om de source van de shell (shell.cc) te printen.
{ int fd = syscall(SYS_open, "shell.cc", O_RDONLY, 0755); // Gebruik de SYS_open call om een bestand te openen.
  char byte[1];                                           // 0755 zorgt dat het bestand de juiste rechten krijgt (leesbaar is).
  while(syscall(SYS_read, fd, byte, 1))                   // Blijf SYS_read herhalen tot het bestand geheel gelezen is,
    std::cout << byte; }                                  //   zet de gelezen byte in "byte" zodat deze geschreven kan worden.
