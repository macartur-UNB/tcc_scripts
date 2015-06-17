from os import mkdir
from os import path
from os import system

number_of_files = 10**4
number_of_includes = 3

folder =  "./pragma-only/"

include_directory = folder+"include"
include_path = folder+"include/{0}.h"
path_main_file = folder+"main.cpp"

content_of_include = """#pragma once
const int int{0} = {0};
"""

end_of_main_file = "int main() {\n}"
header = """#include "{0}.h"\n"""

def verify_directory(path_name):
    if not path.exists(path_name):
        mkdir(path_name)

def create_include_file(path,content):
    f =  open(path,"w+")
    f.write (content)
    f.close()

def create_includes():
    #create directory
    # create all files
    for number in range(0,number_of_files):
        path = include_path.format(str(number))
        content = content_of_include.format(str(number))
        create_include_file(path,content)
    
def create_main_file():
    #open main.cpp
    main = open(path_main_file,"w+")

    #write includes 3 times
    for number in range(0,number_of_files):
        for x in range(0,number_of_includes):
            content = header.format(str(number))
            main.write(content)

    #write end of file
    main.write(end_of_main_file)

    #close main.cpp
    main.close()
def copy_util_files():                                                           
    command = "cp util/* "                                                       
    command += folder                                                            
    system(command)                                                              
                      

def main():
    verify_directory(folder)
    verify_directory(include_directory)
    create_includes()
    create_main_file()
    copy_util_files()

if __name__ == "__main__":
    main()
