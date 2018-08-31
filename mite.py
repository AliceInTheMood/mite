# IMPORTS

from sys import platform, stdin
from os import getcwd, listdir, mkdir

if platform == "esp8266":
    from machine import Pin

# GLOBAL VARIABLES

_version = '0.0.15'
fileName = " "
lineBuffer = []
lineContext = []
gpioCheck = []
ioLog = []

# FUNCTIONS FOR TERMINAL STYLES AND PRESENTATION

def screen(head, body, tail):  # PRINT THE APPLICATION SCREEN

    buffer = ("\033[48;5;25;1m" +
              " " + t(head[0], 19) +
              "\033[48;5;2;1m" +
              " " + head[1] + " " + t(head[2], (19 - len(head[1]))) +
              " " + head[3] + " " + t(head[4], (19 - len(head[3]))) +
              " " + head[5] + " " + t(head[6], (19 - len(head[5]))) +
              "\033[0m" + "\n" + spacer80(" ") + "\n")

    for i in body:
        buffer = buffer + i + "\n"

    buffer = buffer + spacer80(" ") + "\n" + \
                ("\033[48;5;237;38;5;25;1m [7] " +
                 "\033[38;5;255m" + t(tail[0], 22) + " " +
                 "\033[38;5;25;1m [8] " +
                 "\033[38;5;255m" + t(tail[1], 22) + " " +
                 "\033[38;5;25;1m[9] " +
                 "\033[38;5;255m" + t(tail[2], 22) +
                 "\033[0m" + "\n" +
                 "\033[48;5;234;38;5;25;1m [4] " +
                 "\033[38;5;255m" + t(tail[3], 22) + " " +
                 "\033[38;5;25;1m [5] " +
                 "\033[38;5;255m" + t(tail[4], 22) + " " +
                 "\033[38;5;25;1m[6] " +
                 "\033[38;5;255m" + t(tail[5], 22) +
                 "\033[0m" + "\n" +
                 "\033[48;5;237;38;5;25;1m [1] " +
                 "\033[38;5;255m" + t(tail[6], 22) + " " +
                 "\033[48;5;237;38;5;25;1m [2] " +
                 "\033[38;5;255m" + t(tail[7], 22) + " " +
                 "\033[48;5;237;38;5;25;1m[3] " +
                 "\033[38;5;255m" + t(tail[8], 22) +
                 "\033[0m" + "\n" +
                 "\033[48;5;234;38;5;25;1m [0] " +
                 "\033[38;5;255m" + t(tail[9], 22) + " " +
                 "\033[48;5;234;38;5;25;1m [,] " +
                 "\033[38;5;255m" + t(tail[10], 22) + " " +
                 "\033[48;5;234;38;5;25;1m[.] " +
                 "\033[38;5;255m" + t(tail[11], 22) +
                 "\033[0m")

    print(buffer)


def line(string):  # FORMAT A STRING INTO A LINE

    return "\033[48;5;234;1m " + t(string, 79) + "\033[0m"


def block(tittle, array):  # FORMAT ARRAY INTO 4 ELEMENT BLOCKS

    new = []
    while len(array) > 4:
        element = array[:4]
        new.append(element)
        array = array[4:]
    array.append("")
    array.append("")
    array.append("")
    new.append(array)
    result = [line(tittle), spacer80(" ")]
    for i in range(0, len(new)):
        result.append("\033[48;5;234;38;5;25;1m> \033[38;5;255m" +
                      t(new[i][0], 19) + "\033[0m" +
                      "\033[48;5;234;38;5;25;1m> \033[38;5;255m" +
                      t(new[i][1], 19) + "\033[0m" +
                      "\033[48;5;234;38;5;25;1m> \033[38;5;255m" +
                      t(new[i][2], 19) + "\033[0m" +
                      "\033[48;5;234;38;5;25;1m> \033[38;5;255m" +
                      t(new[i][3], 18) + "\033[0m")
    return result


def code(tittle, array):  # FORMATTED CODE

    result = [line(tittle), spacer80(" ")]
    for i in range(0, len(array)):
        result.append("\033[48;5;237m" + t(" %s" % i, 6) +
                      "\033[48;5;234m " + t(array[i], 74) + "\033[0m")
    return result


def t(text, num):  # TRUNCATE TEXT OR ADD SPACE

    length = (len(text)+1)
    if length >= num:
        text = "..." + text[length - num + 3:]
    if length < num:
        for i in range(0, num - length):
            text = text + " "
    return text


def spacer80(char):  # 80 CHAR SPACER

    s = ""
    for i in range(0, 79):
        s = s + char
    return "\033[48;5;234m" + s + "\033[0m"


# FUNCTIONS

def get_input():  # GET USER INPUT

    option = stdin.readline(1)
    if option != '\n':
        return option


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


# MAIN SCREEN

def main():

    head = ["[mite] " + _version,
            "Platform:", platform,
            "", "",
            "", ""]

    body = [line("Choose an option:")]

    tail = ["File Manager", "Code Editor", "",
            "", "", "",
            "I/O Manager", "", "",
            "Quit", "", ""]

    screen(head, body, tail)
    option = get_input()

    while True:
        if option == '0':
            quit()
        if option == '\n':
            pass
        if option == '7':
            file_manager()
        if option == '8':
            code_editor("Code")
        if option == '1':
            io_manager()
        else:
            option = get_input()


# FILE MANAGER

def file_manager():

    head = ["File Manager",
            " Elements:", "%s" % len(listdir(getcwd())),
            "Files: ", "%s" % len(parse_dir()[0]),
            "Directories: ", "%s" % len(parse_dir()[1])]

    body = block(getcwd() + ": ", listdir(getcwd()))

    tail = ["Choose /dir", "Make /dir", "",
            "Open File", "Make File", "Remove File",
            "", "", "",
            "Return", "", ""]

    screen(head, body, tail)
    option = get_input()

    while True:
        if option == '0':
            main()

        if option == '8':  # MAKE DIR
            newdir = input()
            mkdir(newdir)
            file_manager()

        if option == '5':  # MAKE FILE
            file = input("Choose a name for the new file: ")
            f = open(str(file), 'w')
            f.close()
            file_manager()

        else:
            option = get_input()


# CODE EDITOR

def code_editor(mode):

    head = ["Code Editor",
            "", "",
            "Language:", "",
            "Lines: ", "%s" % len(lineBuffer)]

    body = []

    if mode == "Code":
        body = code(" ",lineBuffer)
    if mode == "Search":
        print("\033[48;5;234m" +
              t(" The following lines of code match your query: ", 80) +
              "\033[0m")
        print(spacer80(" "))
        for i in range(0, len(lineContext)):
            print("\033[48;5;237m" + t(" %s" % lineContext[i], 6) +
                  "\033[48;5;234m " +
                  t(lineBuffer[int(lineContext[i])], 74) +
                  "\033[0m")

    lineContext.clear()

    tail = ["Insert Line", "Remove Line", "Edit Line",
            "Join Line", "", "",
            "Save", "", "Search",
            "Return", "", ""]

    screen(head,body,tail)
    option = get_input()

    while True:
        if option == '0':  # RETURN TO MAIN SCREEN
            main()

        if option == '7':  # INSERT LINE
            line = input("Type your code: \n")
            lineBuffer.append(str(line))
            code_editor("Code")

        if option == '8':  # REMOVE LINE
            line = input("Remove Line: ")
            del lineBuffer[int(line)]
            code_editor("Code")

        if option == '9':  # EDIT LINE
            num = input("Choose a existent line to edit: ")
            line = input("Replace Line" + str(num) + ": ")
            print("")
            try:
                lineBuffer[int(num)] = line
            except:
                print("The line N°" + num + " doesn't exist!")
            code_editor("Code")

        if option == '3':  # SEARCH
            query = input("Search in code for : ")
            for i in range(0, len(lineBuffer)):
                if query in lineBuffer[i]:
                    lineContext.append(str(i))
            code_editor("Search")

        if option == '4':  # JOIN LINE
            num1 = input("Input an existent line: ")
            num2 = input("Input a line to join the previous Line:  ")
            try:
                lineBuffer[int(num1)] = lineBuffer[int(num1)] + " " + \
                                        lineBuffer[int(num2)]
                del lineBuffer[int(num2)]
            except:
                print("A line selected doesn't exist!")
            code_editor("Code")

        if option == '1':  # SAVE
            fileName = input("Name for the new file \
                             (don't forget the extension) : ")
            f = open(fileName, 'w')
            f.writelines("\n".join(lineBuffer))
            code_editor("Code")

        else:
            option = get_input()


def io_manager():

    if platform == "esp8266":
        gpioCheck = [0, 2, 4, 5, 11, 12, 13, 14, 15, 16]
    else:
        print(platform + " platform not supported!")
        main()

    head = ["IO Manager",
            "Platform: ",platform,
            "GPIO: ",str(len(gpioCheck)),
            "",""]
    body = code("Recent Activity: ", ioLog)
    tail = ["Configure GPIO","Set GPIO","",
            "","","",
            "","","",
            "Return","",""]

    screen(head,body,tail)
    options = get_input()

    while True:
        if options == '0':  # RETURN
            main()

        if options == '7':  # READ GPIO
            gpio = input("Enter a GPIO number: ")
            if int(gpio) != any(gpioCheck):
                print("GPIO" + gpio) + " not available"
                io_manager()
            ioLog.append("GPIO" + gpio + "current value = " +
            Pin(int(gpio), Pin.IN).value())
            io_manager()

        if options == '8':  # SET GPIO
            gpio = input("Enter a GPIO number: ")
            if int(gpio) != any(gpioCheck):
                print("GPIO" + gpio) + " not available"
                io_manager()
            state = input("[1] ON [0] OFF")
            if state:
                Pin(int(gpio), Pin.OUT).on()
                ioLog.append("GPIO" + gpio + " now set on")
            else:
                Pin(int(gpio), Pin.OUT).off()
                ioLog.append("GPIO" + gpio + " now set off")
            io_manager()

        else:
            get_input()


# INIT
main()
