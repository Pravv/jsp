def zad27(d1, d2):
    d1 = datetime.datetime.strptime(d1, "%d-%m-%Y")
    d2 = datetime.datetime.strptime(d2, "%d-%m-%Y")
    return abs((d2 - d1).days)
	
zad27("10-10-1000", "12-10-100")