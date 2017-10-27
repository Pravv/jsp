def zad18():
    i = 0
    # drukujemy wszystkie liczby parzyste mniejsze od 10
    while i < 10:
        if not i % 2:  # reszta z dzielenia != 0 -> True
            print(i)  # pomiń liczby nieparzyste

        i += 1  # zwiększ i o jeden
		
zad18()