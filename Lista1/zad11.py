def zad11():
    myList = list(range(0, 100, 3))
    del myList[5::3]
    avg = sum(myList) / len(myList)
	
zad11()