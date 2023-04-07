import random


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
    for word in generator(text, sep=" "):
        print(word)
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)

    text = "Lorem Ipsum Lorem Ipsum"
    for word in generator(text, sep=" ", option="unique"):
        print(word)
