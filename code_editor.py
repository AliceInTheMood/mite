# ###---### CODE EDITOR ###---### #

# IMPORTS

from mite import framework, main

# GLOBAL VARIABLES

searchMode = False
lineBuffer = []
lineContext = []


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

    global searchMode

    if searchMode:
        searchMode = False
        body = [framework.line("The following lines of code match your query:"),
                framework.spacer80(" ")]
        for i in range(0, len(lineContext)):
            body.append("\033[48;5;237m" + framework.t(" %s" % lineContext[i], 6) +
                        "\033[48;5;234m " +
                        framework.t(lineBuffer[int(lineContext[i])], 74) +
                        "\033[0m")
    else:
        body = framework.code(" ", lineBuffer)

    lineContext.clear()

    tail = ["Insert Line", "Remove Line", "Edit Line",
            "Join Line", "", "",
            "Save", "", "Search",
            "Return", "Reload", ""]

    framework.screen(head, body, tail)

    framework.option_handler(
        insert_line,
        del_line,
        edit_line,
        join_line,
        framework.none,
        framework.none,
        save_code,
        framework.none,
        search_line,
        main,
        code_editor,
        framework.none)
