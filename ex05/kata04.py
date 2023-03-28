kata = (0, 4, 132.42222, 10000, 12345.67)

if __name__ == "__main__":
    line  = 'module_%02d, ex_%02d : %5.2f, %.2e, %.2e' % (kata[0], kata[1], kata[2], kata[3], kata[4])
    print(line)

