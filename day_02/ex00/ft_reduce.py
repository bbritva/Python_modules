def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    if not hasattr(iterable, "__iter__"):
        raise TypeError("ft_map() argument #2 must support iteration")
    if not callable(function_to_apply):
        raise TypeError("ft_map() argument #1 must be callable")
    try:
        partial_result = iterable[0]
        for i in iterable[1:]: # Skip the first element
            partial_result = function_to_apply(partial_result, i)
    except TypeError:
        return None
    except IndexError:
        return None
    return partial_result

if __name__ == "__main__":
    print(ft_reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
    print(ft_reduce(lambda x, y: x + y, []))
    print(ft_reduce(lambda x, y: x + y, [1]))
    print(ft_reduce(lambda x, y: x + y, [1, 2]))
    print(ft_reduce(lambda x, y: x + y, [1, 2, 3]))
    print(ft_reduce(lambda x, y: x + y, [1, 2, 3, 4]))
    print(ft_reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
    lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    print(ft_reduce(lambda u, v: u + v, lst))
    print(ft_reduce((lambda x, y: x + y), [1]))
    print(ft_reduce((lambda x, y: x * y), [1, 2, 3, 4]))