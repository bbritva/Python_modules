from termcolor import cprint
from matrix import Matrix, Vector


if __name__ == "__main__":
    m = Matrix([[1.0, 2.0], [3.0, 4.0]])
    print(m)
    print(m.T())
    m1 = Matrix([[0.0, 1.0, 2.0, 3.0],
                [0.0, 2.0, 4.0, 6.0]])
    m3 = Matrix([[6.0, 1.0, 66.0, 3.0],
                [6.0, 2.0, 66.0, 6.0]])
    m2 = Matrix([[0.0, 1.0],
                [2.0, 3.0],
                [4.0, 5.0],
                [6.0, 7.0]])
    print("m1 * m2")
    print(m1 * m2)
    print("m1 + m3")
    print(m1 + m3)
    print("m1 - m3")
    print(m1 - m3)
    print("m1 / 3")
    print(m1 / 3)
    print("3 / m3")
    print(3 / m3)


    v = Vector([[1.0, 2.0, 3.0, 4.0]])
    print(v)
    print(v.T())

    v1 = Vector([[1, 2, 3]]) # create a row vector
    v2 = Vector([[1], [2], [3]]) # create a column vector
    print(v1)
    print(v2)
    print(v1.T())
    v1 = Vector([[1], [2], [3]])
    v2 = Vector([[0], [4], [8]])

    print("v1 * v2")
    print(v1 * v2)
    print("v1 + v2")
    print(v1 + v2)
    print("v1 - v2")
    print(v1 - v2)
    print("v1 / 2")
    print(v1 / 2)
    print("3 / v2")
    print(3 / v2)

    m1 = Matrix([[0.0, 1.0, 2.0],
    [0.0, 2.0, 4.0]])
    v1 = Vector([[1], [2], [3]])
    print("m1 * v1")
    print(m1 * v1)