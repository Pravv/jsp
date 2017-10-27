def zad19():
    # lista zakupów
    grocery = ['jajka', 'mleko', 'chleb', 'maslo', 'piwo']
    # ilość sztuk
    n_items = []
    # zakazane produkty
    prohibited = ['wódka', 'piwo', 'wino']

    # w pętli pytamy użytkownika, ile sztuk danego produktu chce kupić
    for product in grocery:
        if product in prohibited:
            n_items.append("0")
        else:
            print("Produkt " + product + ": sztuk = ")
            n_items.append(input())
            # wydrukuj na ekranie komunikat: "Produkt [nazwa produktu]: sztuk = "
            # pobierz liczbę od użytkownika i zapisz w n_items
            # pomiń produkty zakazane (i automatycznie przyjmij ilość = 0)

    # drukujemy listę zakupów

    print("{:-^50}".format("Lista zakupów"), end="\n\n")

    index = 0
    while index < len(grocery):
        print(str(index) + '. ' + grocery[index] + ': ' + n_items[index])
        index += 1  # This is the same as count = count + 1
        # w pętli wydrukuj: [lp]. [nazwa produktu]: [ilość]
        # czyli np.: 1. jajka: 5 itd.
		
zad19()