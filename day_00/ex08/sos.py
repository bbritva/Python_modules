import sys

morse_dict = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----'}


def toMorse(c):
    if (c.isspace()):
        return ('/ ')
    elif (c.isalnum()):
        return (morse_dict[c] + ' ')
    else:
        print('ERROR')
        sys.exit(0)


if __name__ == "__main__":
    arr = sys.argv
    del arr[0]
    line = ' '.join(arr).upper()
    morse = ''
    for c in line:
        morse += toMorse(c)
    if morse:
        print(morse)
