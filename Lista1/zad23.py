def my_min(lhs, rhs):
    return rhs if rhs < lhs else lhs


def multi_min(*args):
    min = sys.maxsize
    for arg in args:
        min = my_min(min, arg)
    return min
	
print(multi_min(1, 2, 3, 4, 5, 6, 7, 8, 35234))