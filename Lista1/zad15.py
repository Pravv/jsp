def zad15():
    x = 2
    y = x
    print(x, y, id(x), id(y))
    y = 3
    print(x, y, id(x), id(y))

    x = [1, 2]
    y = x
    print(x, y, id(x), id(y))
    y[1] = 3
    print(x, y, id(x), id(y))
	
zad15()