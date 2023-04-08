import random

from termcolor import cprint


def generator(text, sep=" ", option=None):
    if not isinstance(text, str) or not isinstance(sep, str):
        yield "ERROR"
    arr = text.split(sep)
    if not option:
        for word in arr:
            yield word
    elif option == "shuffle":
        while len(arr) > 0:
            i = random.randint(0, len(arr) - 1)
            yield arr[i]
            del arr[i]
    elif option == "unique":
        newArr = []
        for word in arr:
            if not word in newArr:
                newArr.append(word)
        for word in newArr:
            yield word
    else:
        yield "ERROR"


if __name__ == '__main__':
    text = "Le Lorem Ipsum est simplement du faux texte."
    cprint("Simple test", "green")
    for word in generator(text, sep=" "):
        print(word)
    cprint("\nShuffle test", "green")
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    cprint("\nShuffle test2 (shouldn't be the same)", "green")
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)

    cprint("\nUnique test", "green")
    text = "Lorem Ipsum Lorem Ipsum"
    for word in generator(text, sep=" ", option="unique"):
        print(word)

    cprint("\nCode_blocks tests:", "black", "on_white")
    txt="This is a simple string for a basic test. Very simple."

    cprint("First test", "green")
    for elem in generator(txt, sep=' '):
        print(f"'{elem}'")

    cprint("\nSecond test", "green")
    for elem in generator(txt, sep='.'):
        print(f"'{elem}'")

    cprint("\nThird test", "green")
    for elem in generator(txt, sep='i'):
        print(f"'{elem}'")

    cprint("\nFourth test", "green")
    for elem in generator(txt, sep='si'):
        print(f"'{elem}'")
