def zad9():
    tup = (0, 1, 2, 3, 4, "pięć", "sześć", "siedem", "osiem", "dziewięć");
    print(tup[0:3])
    print(tup[-2:])
    print(tup[::2])

    print(len(tup))
    print(len(tup[-1]))

    tup[:5] + (5, 6) + tup[-3:]  # łączy 3 tuple w jedną
    tup[:5], (5, 6), tup[-3:]  # printuje 3 osobne tuple

    tup + ""  # nie można append bo tuple są immunable. Operator `+` tworzy nową tuple;

zad9();