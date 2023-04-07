from vector import Vector
from termcolor import colored, cprint


if __name__ == '__main__':
    cprint("Creation tests:", "black", "on_white")
    cprint("Bad values in constructor:", "white", "on_red")
    try:
        vct = Vector([[[[1.]]]])
    except ValueError:
        cprint("ValueError", "red")
    try:
        vct = Vector(-5)
    except ValueError:
        cprint("ValueError", "red")
    try:
        vct = Vector(4, 2)
    except ValueError:
        cprint("ValueError", "red")
    except TypeError:
        cprint("TypeError", "red")
    try:
        vct = Vector([[1], [2], [3]])
    except ValueError:
        cprint("ValueError", "red")
    
    cprint("Good values in constructor:", "white", "on_green")
    vct = Vector([[1.], [2.], [3.]])
    print("input: " + "[[1.], [2.], [3.]] => vct =", vct)
    vct = Vector([[1., 2., 3.]])
    print("input: " + "[[1., 2., 3.]]     => vct =", vct)
    vct = Vector(3)
    print("input: " + "3                  => vct =", vct)
    vct = Vector((10, 16))
    print("input: " + "(10, 16)           => vct =", vct)
    vct = Vector((-10, -5))
    print("input: " + "(-10, -5)          => vct =", vct)

    cprint("\nMethods tests:", "black", "on_white")
    vct1 = Vector([[1.], [2.], [3.]])
    print("vct1 = ", vct1)
    vct2 = Vector([[3.], [4.], [5.]])
    print("vct2 = ", vct2)
    print("dot  = ", vct1.dot(vct2))
    print("Transposed vct1 = ", vct1.T())
    print("Transposed twice vct1 = ", vct1.T().T())
    print("Transposed vct2 = ", vct2.T())

    cprint("\nDunder tests:", "black", "on_white")
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = v1 * 5
    print(v1, "* 5 =",v2)
    v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
    v2 = v1 * 5
    print(v1, "* 5 =",v2)
    v2 = v1 / 2
    print(v1, "/ 2 =",v2)
    print(v1, "/ 0")
    try:
        v2 = v1 / 0.0
    except ZeroDivisionError:
        print("ZeroDivisionError: division by zero.")
    try:
        print("2 / ", v1)
        v2 = 2 / v1
    except NotImplementedError:
        print("NotImplementedError: Division of a scalar by a Vector is not defined here.")

    # Column vector of shape (n, 1)
    print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
    # Expected output
    # (4,1)
    print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
    # Expected output
    # [[0.0], [1.0], [2.0], [3.0]]
    # Row vector of shape (1, n)
    print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
    # Expected output
    # (1,4)
    print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)
    # Expected output
    # [[0.0, 1.0, 2.0, 3.0]]
    # Example 1:
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print(v1.shape)
    # Expected output:
    (4,1)
    print(v1.T())
    # Expected output:
    # Vector([[0.0, 1.0, 2.0, 3.0]])
    print(v1.T().shape)
    # Expected output:
    # (1,4)
    # Example 2:
    v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
    print(v2.shape)
    # Expected output:
    # (1,4)
    print(v2.T())
    # Expected output:
    # Vector([[0.0], [1.0], [2.0], [3.0]])
    print(v2.T().shape)
    # Expected output:
    # (4,1)
    print( "Example 1:")
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
    print(v1.dot(v2))
    # Expected output:
    # 18.0
    v3 = Vector([[1.0, 3.0]])
    v4 = Vector([[2.0, 4.0]])
    print(v3.dot(v4))
    # Expected output:
    # 13.0
    print(repr(v1))
    # Expected output: to see what __repr__() should do
    # [[0.0, 1.0, 2.0, 3.0]]
    print(v1)
    # Expected output: to see w
