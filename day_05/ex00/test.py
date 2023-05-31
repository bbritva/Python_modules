from matrix import Matrix, Vector


if __name__ == "__main__":
    m = Matrix([[1.0, 2.0], [3.0, 4.0]])
    print(m)
    print(m.T())
    m1 = Matrix([[0.0, 1.0, 2.0, 3.0],
                [0.0, 2.0, 4.0, 6.0]])
    m2 = Matrix([[0.0, 1.0],
                [2.0, 3.0],
                [4.0, 5.0],
                [6.0, 7.0]])
    print(m1 * m2)

    m = Matrix([[1.0, 2.0, 3.0, 4.0]])
    print(m)
    print(m.T())

    v1 = Vector([[1, 2, 3]]) # create a row vector
    v2 = Vector([[1], [2], [3]]) # create a column vector
    print(v1)
    print(v2)
    # v3 = Vector([[1, 2], [3, 4]])
