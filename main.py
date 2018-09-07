# ###---### MAIN ###---### #

# IMPORTS

from sys import platform
from mite import framework, file_manager, code_editor


def main():

    head = ["[mite] " + framework._version,
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
        file_manager,
        code_editor,
        framework.none,
        framework.none,
        framework.none,
        framework.none,
        framework.none,
        framework.none,
        framework.none,
        quit,
        framework.none,
        framework.none)
