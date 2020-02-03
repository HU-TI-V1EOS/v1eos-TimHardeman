#!/usr/bin/env python3

import os
import sys
import random
import hashlib
import generate_clues as gc
import re
from subprocess import Popen, PIPE

from subprocess import check_output

def popen2(cmd):
    return Popen(cmd, shell=True, stdout=PIPE, close_fds=True).stdout.read().decode("UTF-8")

def check_hint(clue, hint):
    if (clue == 3):
        count = len(os.listdir("/usr"))
        return int(hint) == count
    elif (clue == 4):
        hostname = open("/etc/hostname", "r").read().strip()
        return hint == hostname
    elif (clue == 5):
        return hashlib.md5(hint.encode()).hexdigest() in ["865c0c0b4ab0e063e5caa3387c1a8741", "7b8b965ad4bca0e41ab51de7b31363a1", "9cefd96d40d0ee1256c8eff1def0312d", "20f011826070657b0f0092278d65ec74"]
    elif (clue == 6):
        return hint == os.getenv("PATH").split(":")[0]
    elif (clue == 7):
        return hint == popen2("which python").strip() or hint == popen2("which python3").strip()
    elif (clue == 8):
        return hashlib.md5(hint.encode()).hexdigest() in ['0512868916a7081afcfb789198de0f37', '865726b2885feef8e8b25b56a2d7c8f8', '4ab7d471b85d867f917bf1a97f4224ec']

    elif (clue == 9):
        return hint == popen2("wc -l /usr/share/dict/words").strip().split(' ')[0]
    elif (clue == 10):
        return hint == popen2("grep -A 1 tactics /usr/share/dict/words").strip().split('\n')[1]
    elif (clue == 11):
        return hashlib.md5(hint.encode()).hexdigest() in ["d86b1ca862b3c45142b5d029e167b097", "92cf65ca941ffa48f947a438d41f54c6", "48b31a14f2559fa440deba1693cdde46", "5245f994cb6cf5036b7128ed7ccd3d8c", "862fca2ccc1e235b07a29c4814033a94", "1a1dcdc69afb9c0bc91589b51f7a9394"]
    elif (clue == 12):
        return hint == popen2("ps -A").split('\n')[1].split(' ')[-1].strip()
    elif (clue == 13):
        return hashlib.md5(hint.encode()).hexdigest() in ["66a4a1a2b442e8d218e8e99100069877", "af5e7df14af034434124fd61b2b2b319"]


if __name__ == "__main__":

    if (len(sys.argv) != 4):
        sys.exit("Need a secret number, clue number, and hint")
    secret_number = int(hashlib.md5(sys.argv[1].encode()).hexdigest(), 16)
    print(secret_number)
    clue_number = int(sys.argv[2])
    hint = sys.argv[3]

    clue_indexes = gc.gen_clue_list(gc.START_CLUE, gc.LAST_CLUE,
                                    gc.CLUE_SPACE, secret_number)
    #print clue_indexes
    if (check_hint(clue_number, hint)):
        print(gc.zero_pad(clue_indexes[clue_number - gc.START_CLUE]))
    else:
        R = random.Random()
        if (type(hint) == str):
            md5 = hashlib.md5(hint.encode())
            hint_number = int(md5.hexdigest(),16)
        R.seed(secret_number + clue_number + hint_number)
        print(gc.zero_pad(R.randint(1, gc.CLUE_SPACE)))
