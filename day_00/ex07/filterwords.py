import string
import sys


if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("ERROR")
    else:
        try:
            lenght = int(sys.argv[2])
            words = filter(lambda word: len(word) > lenght,
                           sys.argv[1].translate(
                str.maketrans('', '', string.punctuation)).split(' '))
            print(list(words))
        except ValueError:
            print('ERROR')
