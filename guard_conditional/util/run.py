#!/usr/bin/python
import os
import sys

number_of_test = 10
make_clang = "{ time make compile_using_clang ;}"
make_gplusplus   ="{ time make;}"


def get_command(clang="g++"):
    command =""

    if "clang" in  clang:
        command+=make_clang
    else:
        command+=make_gplusplus

    command += " 2> tmp.txt; cat tmp.txt |  grep elapsed |"
    command += "sed 's/\(\w*:\w\{2\}.\w\{2\}\)elapsed/\\n\\1\\n/g'"
    command +=" | grep : >> result.txt" 
    return command

def call(command):
    os.system(command) 


def clean_files():
    command = "rm prog tmp.txt"
    os.system(command) 
    

if __name__ == "__main__": 

    if len(sys.argv) > 1:
        command = get_command(sys.argv[1])
    else:
        command = get_command()

    for i in range(number_of_test):
        call(command)
    clean_files()
