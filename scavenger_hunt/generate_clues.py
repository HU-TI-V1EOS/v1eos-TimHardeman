#!/usr/bin/env python3

import os
import re
import sys
import random
import hashlib
from cryptography.fernet import Fernet

START_CLUE = 2
LAST_CLUE = 14
CLUE_SPACE = 100000
FIRST_CLUE = 12345

def zero_pad(clue):
    l = len(str(clue))
    m = len(str(CLUE_SPACE)) - 1
    if l < m:
        return "0"*(m-l) + str(clue)
    else:
        return str(clue)

def gen_clue_list(first, last, space, secret):
    R = random.Random()
    R.seed(secret)
    clue_indices = []
    for i in range(first, last+1):
        clue_indices.append(R.randint(1, space))
    clue_indices[0] = FIRST_CLUE
    return clue_indices

if __name__ == "__main__":

    if (len(sys.argv) != 2):
        sys.exit("Need a secret number")
    secret_number = int(hashlib.md5(sys.argv[1].encode()).hexdigest(), 16)
    print(secret_number)

    result = ""
    try:
        result = os.stat("clues")
    except:
        pass

    if (result):
        sys.exit("Clues folder already exists.")

    if (not result):
        os.mkdir("clues")

    clue_indices = gen_clue_list(START_CLUE, LAST_CLUE,
                                 CLUE_SPACE, secret_number)

    template_names = os.listdir(".clue-templates")
    template_names.sort()
    template_data = []

    f = Fernet(open(".key", "rb").read())

    for t in template_names:
        if re.search(".*.md.asc$", t):
            data = open(".clue-templates/" + t, "rb").read()
            template_data.append(f.decrypt(data).decode('UTF-8'))

    print("Hiding clues...")
    for i in range(0, CLUE_SPACE):
        dir_name = "clues/" + \
            "0"*(len(str(CLUE_SPACE))-1 - len(str(i))) + str(i)
        os.mkdir(dir_name)
        file_name = open(dir_name + "/clue", "w")
        if (i not in clue_indices):
            file_name.write("Nothing to see here.\n")
        else:
            template_index = clue_indices.index(i)
            if (template_index < len(template_data)):
                if (template_index == 2):
                    file_name.write(template_data[template_index]
                                    .format(zero_pad(clue_indices[0]),
                                            zero_pad(clue_indices[1])))
                elif (template_index == 12):
                    file_name.write(template_data[template_index]
                                    .format(hashlib.md5("/scavenger_hunt/{}"
                                        .format(secret_number).encode())
                                        .hexdigest()))
                else:
                    file_name.write(template_data[template_index])
            else:
                file_name.write("Clue: \n")
    print("Done hiding clues.")
