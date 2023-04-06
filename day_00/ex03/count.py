import string
import sys


def text_analyzer(line=""):
    """This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""

    uppers = 0
    lowers = 0
    spaces = 0
    puncts = 0

    if not isinstance(line, str):
        print("AssertionError: argument is not a string")
        return
    if not line:
        line = input("What is the text to analyze? ")
    for c in line:
        if c.isupper():
            uppers += 1
        elif c.islower():
            lowers += 1
        elif c.isspace():
            spaces += 1
        elif c in string.punctuation:
            puncts += 1
    print("The text contains {} character(s):".format(str(len(line))))
    print("- {} upper letter(s)".format(str(uppers)))
    print("- {} lower letter(s)".format(str(lowers)))
    print("- {} punctuation mark(s)".format(str(puncts)))
    print("- {} space(s)".format(str(spaces)))


if __name__ == "__main__":
    if (len(sys.argv) == 2):
        text_analyzer(sys.argv[1])
    elif (len(sys.argv) < 2):
        text_analyzer()
    else:
        print("AssertionError: more than one argument are provided")
