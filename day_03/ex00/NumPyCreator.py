import numpy


class NumPyCreator:
    def __init__(self):
        numpy.warnings.filterwarnings('ignore', category=numpy.VisibleDeprecationWarning)

    def check_nested_list(self, lst):
        lenght = len(lst[0])
        for i in lst[1:]:
                if len(i) != lenght:
                    return False
        return True

    def check_type(self, lst):
        if hasattr(lst, "__iter__"):
            if len(lst) > 0 and  hasattr(lst[0], "__iter__"):
                return self.check_nested_list(lst)
            else:
                return True
        return False

    def from_list(self, lst, dtype=None):
        return numpy.array(lst, dtype=dtype) if self.check_type(lst) else None

    def from_tuple(self, tpl, dtype=None):
        return numpy.array(tpl, dtype=dtype) if self.check_type(tpl) else None

    def from_iterable(self, itr, dtype=None):
        return numpy.array(itr, dtype=dtype) if self.check_type(itr) else None

    def from_shape(self, shape, value=0, dtype=None):
        return numpy.full(shape, value, dtype=dtype)

    def random(self, shape):
        return numpy.random.random(shape)

    def identity(self, n, dtype=None):
        return numpy.identity(n, dtype=dtype)
    

if __name__ == "__main__":
    npc = NumPyCreator()
    print(npc.from_list([[1,2,3],[6,3,4]]))
    # Output :
    # array([[1, 2, 3],
    # [6, 3, 4]])
    print(npc.from_list([[1,2,3],[6,4]]))
    # Output :
    # None
    print(npc.from_list([[1,2,3],['a','b','c'],[6,4,7]]))
    # Output :
    # array([['1','2','3'],
    # ['a','b','c'],
    # ['6','4','7'], dtype='<U21'])
    print(npc.from_list(((1,2),(3,4))))
    # Output :
    None
    print(npc.from_tuple(("a", "b", "c")))
    # Output :
    # array(['a', 'b', 'c'])
    print(npc.from_tuple(["a", "b", "c"]))
    # Output :
    # None
    print(npc.from_iterable(range(5)))
    # Output :
    # array([0, 1, 2, 3, 4])
    shape=(3,5)
    print(npc.from_shape(shape))
    # Output :
    # array([[0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0]])
    print(npc.random(shape))
    # Output :
    # array([[0.57055863, 0.23519999, 0.56209311, 0.79231567, 0.213768 ],
    # [0.39608366, 0.18632147, 0.80054602, 0.44905766, 0.81313615],
    # [0.79585328, 0.00660962, 0.92910958, 0.9905421 , 0.05244791]])
    print(npc.identity(4))
    # Output :
    # array([[1., 0., 0., 0.],
    # [0., 1., 0., 0.],
    # [0., 0., 1., 0.],
    # [0., 0., 0., 1.]])