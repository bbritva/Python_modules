from vector import Vector
from termcolor import colored, cprint


if __name__ == '__main__':
    cprint("Creation tests:", "black", "on_white")
    print(colored("Bad values in constructor:", "red"))
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
    vct = Vector([[1.], [2.], [3.]])
    print(vct)
    print(vct.T())
    vct.dot(5)
    print(vct)
    vct = vct.T()
    print(vct)
    vct = vct.T()
    print(vct)
    vct = Vector([[1., 2., 3.]])
    print(vct)
    print(vct.T())
    vct = Vector(3)
    print(vct)
    vct = Vector((10, 16))
    print(vct)
    vct = Vector((-10, 16))
    print(vct)
    vct = Vector((-20, -16))
    print(vct)
    vct.dot(5)
    print(vct)
