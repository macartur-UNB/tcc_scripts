import glob
import sys
from datetime import datetime
from os.path import exists
from os import getcwd, chdir, makedirs, system
from shutil import rmtree

command = " python {} "
current_dir = getcwd()
output = "{}/results".format(current_dir)
MAX = 10

def make_dirs():
    if(not exists(output)):
        makedirs(output)

def go_back():
    print("Changed dir ..")
    chdir("..")

def go_folder(name):
    chdir(name)
    print("changed dir {}".format(name))


def compile():
    compile_command = "make"
    system(compile_command)

def clean():
    clean_command = "make clean"
    system(clean_command)


def get_time():
    return datetime.now()

def save_result(file,count,elapsed):
    message = "{}: {}\n".format(count,elapsed.total_seconds())
    print(message)
    file_ = open("{}/{}.txt".format(output,file),"a+")
    file_.write(message)
    file_.close()

def remove_dir(name):
    print("Removing dir "+name)
    rmtree(name)


make_dirs()
for file in glob.glob("*.py"):
    if file == "run.py":
        continue
    system(command.format(file))

    dir_name = file[:-3]
    go_folder(dir_name)
    for count in range(0,MAX):
        start = get_time()
        print(getcwd())
        compile()
        end= get_time()
        clean()
        save_result(dir_name,count,end-start)
    go_back()
    remove_dir(dir_name)
