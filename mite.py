# [mite] - Zunder 2018

# IMPORTS

from sys import platform, stdin
from os import getcwd, listdir, mkdir

if platform == "esp8266":
    from machine import Pin

# GLOBAL VARIABLES

_version = '0.0.17'
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


def option_handler(o7, o8, o9, o4, o5, o6, o1, o2, o3, o0, oc, od):  # GET USER OPTION

    option = stdin.readline(1)
    while True:

        if option == '7':
            o7()
        if option == '8':
            o8()
        if option == '9':
            o9()

        if option == '4':
            o4()
        if option == '5':
            o5()
        if option == '6':
            o6()

        if option == '1':
            o1()
        if option == '2':
            o2()
        if option == '3':
            o3()

        if option == '0':
            o0()
        if option == ',':
            oc()
        if option == '.':
            od()

        else:
            option = stdin.readline(1)
            

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


def none():  # EMPTY FUNCTION
    print('[ERROR] Option not available, try again!')


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

    option_handler(file_manager, code_editor, none,
                   none, none, none,
                   io_manager, none, none,
                   quit, none, none)


# ###---### FILE MANAGER ###---### #

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

    body = block(getcwd() + ": ", listdir(getcwd()))

    tail = ["Choose /dir", "Make /dir", "",
            "", "Make File", "Remove File",
            "", "", "",
            "Return", "", ""]

    screen(head, body, tail)

    option_handler(none, make_dir, none,
                   none, make_file, none,
                   io_manager, none, none,
                   main, none, none)


# ###---### CODE EDITOR ###---### #

searchMode = False


def insert_line():  # INSERT LINE
    line = input("Type your code: \n")
    lineBuffer.append(str(line))
    code_editor()


def del_line():  # DELETE LINE
    line = input("Remove Line: ")
    del lineBuffer[int(line)]
    code_editor()


def edit_line():  # EDIT LINE
    num = input("Choose a existent line number to edit: ")
    if check_buffer(num) == 0:
        print("Please Choose an Option: \n")
        print("[a] Append [p] Prepend [s] Replace specific [r] Replace all")
        opt = input("\n")

        if opt == "r":
            line = input("Replace line with : \n")
            print("")
            lineBuffer[int(num)] = line
        else:
            print("[ERROR] Please select a valid option")
    if check_buffer(num) == 2:
        print("[ERROR] " + str(num) + " is not a valid number")
    else:
        print("[ERROR] Line N°" + str(num) + " doesn't exist yet")
    code_editor()


def search_line():  # SEARCH LINE
    query = input("Search in code for : ")
    for i in range(0, len(lineBuffer)):
        if query in lineBuffer[i]:
            lineContext.append(str(i))
    global searchMode
    searchMode = True
    code_editor()


def join_line():  # JOIN LINE
    num1 = input("Input an existent line: ")
    num2 = input("Input a line to join the previous Line:  ")
    try:
        lineBuffer[int(num1)] = lineBuffer[int(num1)] + " " + \
                                lineBuffer[int(num2)]
        del lineBuffer[int(num2)]
    except:
        print("A line selected doesn't exist!")
    code_editor()


def save_code():  # SAVE FILE
    filename = input("Name for the new file \
               (don't forget the extension) : ")
    f = open(filename, 'w')
    f.writelines("\n".join(lineBuffer))
    code_editor()


def check_buffer(x):  # CHECK EXISTENCE IN LINE BUFFER
    if x.isdigit():
        if int(x) < len(lineBuffer):
            return 0  # Line x exist within the buffer
        else:
            return 1  # Line x doesn't exist
    else:
        return 2  # x is a string, not a valid number


def code_editor():

    head = ["Code Editor",
            "", "",
            "Language:", "",
            "Lines: ", "%s" % len(lineBuffer)]

    body = []

    global searchMode

    if searchMode == True:
        body = [line("The following lines of code match your query:"),
                 spacer80(" ")]
        for i in range(0, len(lineContext)):
            body.append("\033[48;5;237m" + t(" %s" % lineContext[i], 6) +
                  "\033[48;5;234m " +
                  t(lineBuffer[int(lineContext[i])], 74) +
                  "\033[0m")
        searchMode = False
    else:
        body = code(" ", lineBuffer)

    lineContext.clear()

    tail = ["Insert Line", "Remove Line", "Edit Line",
            "Join Line", "", "",
            "Save", "", "Search",
            "Return", "Reload", ""]

    screen(head, body, tail)

    option_handler(insert_line, del_line, edit_line,
                   join_line, none, none,
                   save_code, none, search_line,
                   main, code_editor, none)


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
