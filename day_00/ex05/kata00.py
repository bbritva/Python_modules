kata = (19, 42, 21)

if __name__ == "__main__":
    line = "The {} numbers are: {}".format(
        len(kata), ', '.join('{}'.format(k) for k in kata))
    print(line)
