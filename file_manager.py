# ###---### FILE MANAGER ###---### #

# IMPORTS

from os import getcwd, listdir, mkdir
import framework
import main

# GLOBAL VARIABLES

_version = "0.1.0"


# FUNCTIONS

def parse_dir():  # SPLIT FILES AND DIRECTORIES

    dirs = []
    files = []
    result = []
    for i in listdir(getcwd()):
        if i[:1] == ".":
            dirs.append(i)
        elif any([i == "LICENSE"]):  # ADD COMMON FILES WITHOUT .EXTENSION
            files.append(i)
        elif any([i[-1:] == ".", i[-2:-1] == ".",
                  i[-3:-2] == "."]):
            files.append(i)
        else:
            dirs.append(i)
    result.append(files)
    result.append(dirs)
    return result


def make_dir():  # MAKE DIRECTORY
    newdir = input()
    mkdir(newdir)
    file_manager()


def make_file():  # MAKE FILE
    file = input("Choose a name for the new file: ")
    f = open(str(file), 'w')
    f.close()
    file_manager()


def file_manager():

    head = ["File Manager",
            " Elements:", "%s" % len(listdir(getcwd())),
            "Files: ", "%s" % len(parse_dir()[0]),
            "Directories: ", "%s" % len(parse_dir()[1])]

    body = framework.block(getcwd() + ": ", listdir(getcwd()))

    tail = ["Choose /dir", "Make /dir", "",
            "", "Make File", "Remove File",
            "", "", "",
            "Return", "", ""]

    framework.screen(head, body, tail)

    framework.option_handler(
        framework.none,
        make_dir,
        framework.none,
        framework.none,
        make_file,
        framework.none,
        framework.none,
        framework.none,
        framework.none,
        main.main,
        framework.none,
        framework.none)
