from vector import Vector

if __name__ == '__main__':
    vct = Vector([[1.], [2.], [3.]])
    print(vct)
    vct.dot(5)
    print(vct)
    vct = Vector([[1., 2., 3.]])
    print(vct)
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
