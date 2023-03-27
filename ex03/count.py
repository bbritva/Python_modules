import sys

def text_analyzer(line = ""):
    uppers = 0
    lowers = 0
    spaces = 0
    puncts = 0

    if not line:
        print("prompt")
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




