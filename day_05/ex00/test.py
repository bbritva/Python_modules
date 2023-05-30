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

    cprint("\nSubject tests:", "black", "on_white")
    print("shape of [[0.0], [1.0], [2.0], [3.0]] =", Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
    print("values of [[0.0], [1.0], [2.0], [3.0]] =", Vector([[0.0], [1.0], [2.0], [3.0]]).values)
    print("shape of [[0.0, 1.0, 2.0, 3.0]] =", Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
    print("values of [[0.0, 1.0, 2.0, 3.0]] =", Vector([[0.0, 1.0, 2.0, 3.0]]).values)
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print("v1 =", v1, "v1.shape =", v1.shape)
    print("v1 transposed =", v1.T())
    print("v1 transposed shape =", v1.T().shape)
    v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
    print("v2 =", v2, "v2.shape =", v2.shape)
    print("v2 transposed =", v2.T())
    print("v2 transposed shape =", v2.T().shape)

    print( "Example 1:")
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
    print("v1 =", v1)
    print("v2 =", v2)
    print("v1.dot(v2) =",v1.dot(v2))
    v3 = Vector([[1.0, 3.0]])
    v4 = Vector([[2.0, 4.0]])
    print("v3 =", v3)
    print("v4 =", v4)
    print("v3.dot(v4) =",v3.dot(v4))
    print("repr(v1):",repr(v1))

    cprint("\nCode_blocks tests:", "black", "on_white")
    cprint("### # 01.02.00", "green")
    print(Vector([[1. , 2e-3, 3.14, 5.]]).values)
    cprint("### # 01.02.01", "green")
    print(Vector(4).values)
    cprint("### # 01.02.02", "green")
    try:
        (Vector(-1))
    except ValueError:
        cprint("ValueError", "red")
    cprint("### # 01.02.03", "green")
    print(Vector((10, 12)).values)
    cprint("### # 01.02.04", "green")
    try:
        print(Vector((3, 1)).values)
    except ValueError:
        cprint("ValueError", "red")
    cprint("### # 01.02.05", "green")
    try:
        v = Vector((1, 1))
        print(v.values)
    except ValueError:
        cprint("ValueError", "red")
    cprint("### # 01.02.06", "green")
    try:
        Vector((4, 7.1))
    except ValueError:
        cprint("ValueError", "red")
    cprint("### # 01.02.07", "green")
    v = Vector(4)
    print(v.values)
    cprint("### # 01.02.08", "green")
    print(v * 4)
    cprint("### # 01.02.09", "green")
    print(4.0 * v)
    cprint("### # 01.02.10", "green")
    try:
        v * "hi"
    except TypeError:
        cprint("TypeError", "red")
    cprint("### # 01.02.11", "green")
    v = Vector(4)
    v2 = Vector([[1.0], [1.0], [1.0], [1.0]])
    print((v + v2).values)
    try:
        cprint("### # 01.02.12", "green")
    except ValueError:
        cprint("ValueError", "red")
    try:
        v + Vector([0.0, 0.0, 0.0, 0.0])
    except ValueError:
        cprint("ValueError", "red")
    cprint("### # 01.02.13", "green")
    try:
        v + "hello"
    except TypeError:
        cprint("TypeError", "red")
    cprint("### # 01.02.14", "green")
    try:
        v + None
    except TypeError:
        cprint("TypeError", "red")
    cprint("### # 01.02.15", "green")
    try:
        print((v - v2).values != (v2 - v).values)
    except ValueError:
        cprint("ValueError", "red")
    cprint("### # 01.02.16", "green")
    print(Vector(4) / 2)
    cprint("### # 01.02.17", "green")
    print(Vector(4) / 3.14)
    cprint("### # 01.02.18", "green")
    try:
        Vector(4) / 0
    except ZeroDivisionError:
        cprint("ZeroDivisionError", "red")
    cprint("### # 01.02.19", "green")
    try:
        Vector(4) / None
    except TypeError:
        cprint("TypeError", "red")
    cprint("### # 01.02.20", "green")
    try:
        None / Vector(4)
    except NotImplementedError:
        cprint("NotImplementedError", "red")
    cprint("### # 01.02.21", "green")
    try:
        3 / Vector(3)
    except NotImplementedError:
        cprint("NotImplementedError", "red")

