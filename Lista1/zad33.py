import string
from functools import reduce
from collections import Counter
import random
import math
import turtle
import datetime

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

zad33()