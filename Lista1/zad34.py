import string
from functools import reduce
from collections import Counter
import random
import math
import turtle
import datetime

def zad34(n):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(n))
	
print(zad34(42))