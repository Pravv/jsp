def zad31():
    p1x, p1y = map(int, input('koordynaty punktu pierwszego oddzielone spacja: ').split())
    p2x, p2y = map(int, input('koordynaty punktu drugiego oddzielone spacja: ').split())

    return math.sqrt((p1x - p2x) ** 2 + (p1y - p2y) ** 2)

zad31()