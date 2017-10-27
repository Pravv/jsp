def zad14():
    print(sys.getsizeof(0))
    print(sys.getsizeof(2 ** 100))
    print(sys.getsizeof(2 ** 1000))
    print(sys.getsizeof(True))  # typ: long
    print(sys.getsizeof(False))  # typ: int

    print(isinstance(0, int))
    print(isinstance(0, float))
    print(isinstance(0.0, float))
    print(isinstance(True, bool))
    print(isinstance(True, int))
	
zad14()