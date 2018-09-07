# IMPORTS

from sys import stdin

# GLOBAL VARIABLES

_version = '0.1.0'  # AT LAST!!!


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


def none():  # EMPTY FUNCTION
    print('[ERROR] Option not available, try again!')
