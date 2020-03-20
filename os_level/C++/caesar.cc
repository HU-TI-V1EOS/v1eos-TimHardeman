#include <iostream>
#include <string>

std::string translate(std::string line, int argument){
	std::string result = ""; // implementeer dit
	unsigned int i = 0;
	for(unsigned int i = 0; i < line.size(); i++){
        	line[i] = line[i] + argument;

        }
        result.push_back(line[i]);

  return line; }

int main(int argc, char *argv[]){
std::string line;
int argument = std::stoi(argv[1]);

  if(argc != 2)
  { std::cerr << "Deze functie heeft exact 1 argument nodig" << std::endl;
    return -1; }

  while(std::getline(std::cin, line))
  { std::cout << translate(line, argument) << std::endl; } 

  return 0; }

