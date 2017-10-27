import string
from functools import reduce
from collections import Counter
import random
import math
import turtle
import datetime

# zad1
import sys
from random import randint

sum = 2 + 3 + 5 + -8
avg = sum / 4

cosPi = math.cos(math.pi)


# zad2
# `_` w trybie interaktywnym zawiera wynik ostatniej operacji

# zad3
# `round` zaokrągla liczę zmiennoprzecinkową, do najbliższej liczby całkowitej

# zad6
def zad6():
    a = "jeden"
    b = "dwa"
    c = 3

    print(a * b)
    print(a + b)
    print(a * c)
    print(a + c)
    print(a + str(c))


# zad7
def zad7():
    # strip
    str = "___string___"
    print(str.strip('_'))  # string

    # isnumeric
    str = u"this2009"
    print(str.isnumeric())  # false

    str = u"23443434"
    print(str.isnumeric())  # true

    # rjust
    str = 'test'.rjust(25, 'X')  # XXXXXXXXXXXXXXXXXXXXXtest


# zad8
def zad8(a, b):
    P = a * b
    print("Pole prostokąta o bokach " + a + " i" + b + "wynosi" + P)


# zad9
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


# zad10
def zad10():
    students = ['Kasia', 'Basia', 'Marek', 'Darek']
    students.append('Józek')
    students.extend(['Ania', 'Basia'])
    sortedStudents = sorted(students)

    print(sortedStudents[3])
    print(sortedStudents[:2])
    print(sortedStudents[-2:])


# zad11
def zad11():
    myList = list(range(0, 100, 3))
    del myList[5::3]
    avg = sum(myList) / len(myList)


# zad12
def zad12():
    tup = ('a', 'b', 'c', 'd')
    print("".join(tup))
    print(" ".join(tup))
    print(", ".join(tup))

    print("     ".join('0' * 100))


# zad13
def zad13():
    slubowanie = """
	wstępując do wspólnoty akademickiej Uniwersytetu Wrocławskiego, ślubuję uroczyście:
	- zdobywać wiedzę i umiejętności,
	- postępować zgodnie z prawem, tradycją i dobrymi obyczajami akademickimi,
	- dbać o dobre imię Uniwersytetu Wrocławskiego i godność studenta.
	"""

    slubowanie[0].upper()
    print(slubowanie.count(' i '))
    print(slubowanie.count('i'))
    print('Uniwersytet' in slubowanie)
    words = slubowanie.split(' ')
    lines = slubowanie.split('\n')


# zad14
def zad14():
    print(sys.getsizeof(0))
    print(sys.getsizeof(2 ** 100))
    print(sys.getsizeof(2 ** 1000))
    print(sys.getsizeof(True))  # typ: long
    print(sys.getsizeof(False))  # typ: int

    print(isinstance(0, int))
    print(isinstance(0, float))
    print(isinstance(0.0, float))
    print(isinstance(True, bool))
    print(isinstance(True, int))


# zad15
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


# zad16
def zad16():
    even = range(2, 100, 2)
    a, b, c, *d = even
    start, *middle, end = even
    print(start, end)
    print(middle)


# zad18
def zad18():
    i = 0
    # drukujemy wszystkie liczby parzyste mniejsze od 10
    while i < 10:
        if not i % 2:  # reszta z dzielenia != 0 -> True
            print(i)  # pomiń liczby nieparzyste

        i += 1  # zwiększ i o jeden


# zad19
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


# zad20
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


# zad23
def my_min(lhs, rhs):
    return rhs if rhs < lhs else lhs


def multi_min(*args):
    min = sys.maxsize
    for arg in args:
        min = my_min(min, arg)
    return min


# zad24
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def zad24():
    n = 5
    for i in range(n):
        print(fib(i))


def zad27(d1, d2):
    d1 = datetime.datetime.strptime(d1, "%d-%m-%Y")
    d2 = datetime.datetime.strptime(d2, "%d-%m-%Y")
    return abs((d2 - d1).days)


def zad28():
    while True:
        try:
            val = int(input('podaj srednice kola'))
            print('odwod:', math.pi * val, 'pole', math.pi ** 2 * (val / 2))
            return
        except ValueError:
            print('Podaj liczbe!')


def zad29():
    char = input('podaj litere: ')
    vowels = ["a", "e", "i", "o", "u"]
    if char in vowels:
        print('samogloska')
    else:
        print('spolgloska')


def zad30(list):
    return ''.join(list)


def zad31():
    p1x, p1y = map(int, input('koordynaty punktu pierwszego oddzielone spacja: ').split())
    p2x, p2y = map(int, input('koordynaty punktu drugiego oddzielone spacja: ').split())

    return math.sqrt((p1x - p2x) ** 2 + (p1y - p2y) ** 2)

    # zad32


def spherical_to_cartesian(r, angle1, angle2):
    x = r * math.sin(math.radians(angle1)) * math.cos(math.radians(angle2))
    y = r * math.sin(math.radians(angle1)) * math.sin(math.radians(angle2))
    z = r * math.cos(math.radians(angle1))
    return x, y, z


def cartesian_to_spherical(x, y, z):
    r = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    angle1 = math.degrees(math.acos(z / r))
    angle2 = math.degrees(math.atan(y / x))
    return r, angle1, angle2


def handle_spherical_input():
    r = float(input('podaj r:'))
    if r < 0:
        print('zle dane! r musi byc conajmniej rowne 0')
        return

    angle1 = float(input('podaj kat1:'))
    if angle1 not in range(0, 180):
        print('zle dane! kat1 przyjmuje wartosci od 0 do 180')
        return

    angle2 = float(input('podaj kat2:'))
    if angle2 not in range(0, 360):
        print('zle dane! kat2 przyjmuje wartosci od 0 do 360')
        return

    return spherical_to_cartesian(r, angle1, angle2)


def handle_cartesian_input():
    x = float(input('podaj x:'))
    y = float(input('podaj y:'))
    z = float(input('podaj z'))
    return cartesian_to_spherical(x, y, z)


def zad32():
    conversionType = str(input('wybierz strone konwersji (0 - kart->sfer, 1 - sfer->kart): '))

    result = {
        '0': handle_cartesian_input,
        '1': handle_spherical_input,
    }.get(conversionType, lambda: print('zla opcja wybierz 0 albo 1'))

    print('wynik:', result())


# zad33
GRAV_ACC = 9.804


def pos_y(initialSpeed, angle, time):
    vy = initialSpeed * math.sin(math.radians(angle)) * time
    return vy - ((GRAV_ACC * time ** 2) / 2)


def pos_x(initialSpeed, angle, time):
    vx = initialSpeed * math.cos(math.radians(angle))
    return vx * time


def throw_range(initialSpeed, angle):
    return (2 * initialSpeed ** 2 * math.sin(math.radians(angle)) * math.cos(math.radians(angle))) / GRAV_ACC


def flight_time(initialSpeed, angle):
    return (2 * initialSpeed * math.sin(math.radians(angle))) / GRAV_ACC


def max_height(initialSpeed, angle):
    return (initialSpeed ** 2 * math.sin(math.radians(angle)) ** 2) / (2 * GRAV_ACC)


def zad33():
    initialSpeed = float(input('predkosc poczatkowa:'))
    angle = float(input('kat:'))
    print('czas lotu:', flight_time(initialSpeed, angle), 's')
    print('max wysokosc:', max_height(initialSpeed, angle), 'm')

    print('zasieg:', throw_range(initialSpeed, angle), 'm')

    while True:
        time = float(input('czas:'))
        if time == 0:
            return
        print('(', pos_x(initialSpeed, angle, time), 'm, ', pos_y(initialSpeed, angle, time), 'm)')


# zad34
def zad34(n):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(n))


# zad35
def crypt(str, key):
    squared = list(map(lambda char: key[char] if char in key.keys() else char, str))
    return ''.join(squared)


def zad35_crypt(str):
    key = {"a": "y", "e": "i", "i": "o", "o": "a", "y": "e"}
    return crypt(str, key)


def zad35_decrypt(str):
    key = {"a": "y", "e": "i", "i": "o", "o": "a", "y": "e"}
    deklucz = {v: k for k, v in key.items()}
    return crypt(str, deklucz)


def zad36(str):
    return not (set(string.ascii_lowercase).difference(set(str.lower())))


def zad38(str):
    str = str.lower()
    return list(str) == list(reversed(str))


# zad39
def zad39_primes(number):
    factors = []
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number /= divisor
        divisor += 1

    return factors


def zad39_nwd(a, b):
    primesA = zad39_primes(a)
    primesB = zad39_primes(b)
    return reduce(lambda sum, y: sum * y, list((Counter(primesA) & Counter(primesB)).elements()))


def zad39_nww(a, b):
    primesA = zad39_primes(a)
    primesB = zad39_primes(b)
    return reduce(lambda sum, y: sum * y, list((Counter(primesA) | Counter(primesB)).elements()))
