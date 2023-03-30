import sys


def whois(str):
    if (str.isdigit()):
        num = int(str)
        if (num == 0):
            print("I'm Zero.")
        elif (num % 2 == 0):
            print("I'm Even.")
        else:
            print("I'm Odd.")
    else:
        print("AssertionError: argument is not an integer")


if (len(sys.argv) == 2):
    whois(sys.argv[1])
elif (len(sys.argv) > 2):
    print("AssertionError: more than one argument are provided")
