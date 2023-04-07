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
    print(v2)