import sys

if (len(sys.argv) > 1):
    newStr = sys.argv[1];
    for i in range(2, len(sys.argv)):
        newStr += " " + sys.argv[i];
    print (newStr[::-1].swapcase())