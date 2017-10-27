def someName(diff, what):
    if diff > 50:
        print('dużo ' + what)
    elif diff > 10:
        print(what)
    else:
        print('trochę ' + what)


def zad20():
    randomNumber = randint(0, 100)
    guessedNumber = -1
    while guessedNumber != randomNumber:
        print('Guess the number:')
        guessedNumber = int(input())

        diff = math.fabs(randomNumber - guessedNumber)
        if not diff:
            print('Wygrałeś!')
            return

        if randomNumber > guessedNumber:
            someName(diff, 'większa')
        else:
            someName(diff, 'mniejsza')
			
zad20()