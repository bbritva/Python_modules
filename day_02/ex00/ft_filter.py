def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    if not hasattr(iterable, "__iter__"):
        raise TypeError("ft_map() argument #2 must support iteration")
    if not callable(function_to_apply):
        raise TypeError("ft_map() argument #1 must be callable")
    for i in iterable:
        try:
            if function_to_apply(i):
                yield i
        except TypeError:
            yield None

if __name__ == "__main__":
    print(ft_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
    print(list(ft_filter(lambda x: x % 2 == 0, [])))
    print(list(ft_filter(lambda x: x % 2 == 0, [1])))
    print(list(ft_filter(lambda x: x % 2 == 0, [1, 2])))
    print(list(ft_filter(lambda x: x % 2 == 0, [1, 2, 3])))
    print(list(ft_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))
    print(list(ft_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])))
