def zad21():
    length = eval(input("Podaj długość boku: "))
    n_sides = int(input("podaj ilosc bokow: "))  # ilość boków
    N = int(input("ile razy?: "))

    figureAngle = 360 / n_sides
    shiftAngle = 360 / N
    turtle.speed(20)  # ustal prędkość żółwia

    for z in range(N):
        for i in range(n_sides):
            turtle.forward(length)  # narysuj linię o danej długości
            turtle.right(figureAngle)  # obróć się w prawo o dany kąt
        turtle.right(shiftAngle)

    turtle.mainloop()  # nie zamykaj okna po narysowaniu
	
zad21()