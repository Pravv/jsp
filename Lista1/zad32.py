import math

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
	
zad32()