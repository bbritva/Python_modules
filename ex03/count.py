import sys

def text_analyzer(line = ""):
    "This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."

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
        elif not c.isdigit():
            puncts += 1
    print ("The text contains {} character(s):".format(str(len(line))))
    print ("- ", str(uppers), " upper letter(s)")
    print ("- ", str(lowers), " lower letter(s)")
    print ("- ", str(puncts), " punctuation mark(s)")
    print ("- ", str(spaces), " space(s)")




