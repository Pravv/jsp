def zad28():
    while True:
        try:
            val = int(input('podaj srednice kola'))
            print('odwod:', math.pi * val, 'pole', math.pi ** 2 * (val / 2))
            return
        except ValueError:
            print('Podaj liczbe!')

zad28()