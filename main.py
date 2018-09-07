# ###---### MAIN ###---### #

# IMPORTS

from sys import platform
import framework
import code_editor
import file_manager


# GLOBAL VARIABLES

_version = "0.1.0"

def main():

    head = ["[mite] " + _version,
            "Platform:", platform,
            "", "",
            "", ""]

    body = [framework.line("Choose an option:")]

    tail = ["File Manager", "Code Editor", "",
            "", "", "",
            "", "", "",
            "Quit", "", ""]

    framework.screen(head, body, tail)

    framework.option_handler(
        file_manager.file_manager,            # 7
        code_editor.code_editor,              # 8
        framework.none,                       # 9
        framework.none,                       # 4
        framework.none,                       # 5
        framework.none,                       # 6
        framework.none,                       # 1
        framework.none,                       # 2
        framework.none,                       # 3
        quit,                                 # 0
        framework.none,                       # ,
        framework.none)                       # .

