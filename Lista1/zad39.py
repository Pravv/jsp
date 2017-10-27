import string
from functools import reduce
from collections import Counter
import random
import math
import turtle
import datetime

def primes(number):
    factors = []
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number /= divisor
        divisor += 1

    return factors


def nwd(a, b):
    primesA = zad39_primes(a)
    primesB = zad39_primes(b)
    return reduce(lambda sum, y: sum * y, list((Counter(primesA) & Counter(primesB)).elements()))


def nww(a, b):
    primesA = zad39_primes(a)
    primesB = zad39_primes(b)
    return reduce(lambda sum, y: sum * y, list((Counter(primesA) | Counter(primesB)).elements()))

print("nwd 10, 30:", nwd(30, 10))
print("nww 10, 30:", nww(30, 10))