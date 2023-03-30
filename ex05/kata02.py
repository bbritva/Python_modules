kata = (9, 9, 5, 3, 0)

if __name__ == "__main__":
    line = '%02d/%02d/%04d %02d:%02d' % (kata[1],
                                         kata[2], kata[0], kata[3], kata[4])
    print(line)
