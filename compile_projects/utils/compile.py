# *-* encoding: utf8 *-*
from datetime import datetime
from os import getcwd, chdir, makedirs, system
from os.path import exists
from yaml import load

# common variables
MAX_TIMES = 10
current_dir = getcwd()
output = current_dir+"/output/"
config_file = current_dir+"/projects.yaml"


def make_directories():
    if(not exists(output)):
        makedirs(output)


def write_result(message, file_name):
    message += "\n"
    make_directories()
    _file = open(output+file_name, "a+")
    _file.write(message)
    _file.close()


def change_to(directory):
    path = current_dir+"/"+directory
    chdir(path)
    print("Changed to {}".format(directory))


def compile_project(command, project_debug):
    if not project_debug:
        command += " > /dev/null 2> /dev/null"

    system(command)


def clean_projects(command, project_debug):
    if not project_debug:
        command += " > /dev/null 2> /dev/null"

    system(command)


def wait_time():
    command = "sleep 1"
    system(command)


def all_project(file_name):
    with open(file_name, 'r') as stream:
        content = load(stream)
    return content


def set_branch(branch_name):
    command = "git checkout {}".format(branch_name)
    system(command)

def exec_command(command):
    print "Using command %s"%(command)
    system(command)


projects = all_project(config_file)

if not projects:
    print("Need create a projects.yaml with projects attributes")

else:
    for project_name, project in projects.items():
        print("Compiling [ {} ]".format(project_name))

        change_to(project['directory']+"/"+project['makefile'])

        for branch in project['branchs'] :
            set_branch(branch['name'])

            if branch['pre-command']:
                for command in branch['pre-command']:
                    exec_command(command['command'])

            message = "Branch [{}][{}]:".format(branch['name'],branch['description'])

            write_result(message,project_name)

            for times in range(0, MAX_TIMES):

                clean_projects(branch['clean'], project['debug'])
                wait_time()

                start_time = datetime.now()
                compile_project(branch['compile'], project['debug'])
                end_time = datetime.now()

                elapsed = end_time - start_time

                text = "[{}/{}] : {:>4} ms".format(times+1, MAX_TIMES,
                                                      elapsed.total_seconds())

                if not project['debug']:
                    print(text)

                write_result(text, project_name)

            write_result("*"*40+"", project_name)

            if branch['pos-command']:
                for command in branch['pos-command']:
                    exec_command(command['command'])

    print("Finished the result was saved in output folder")
