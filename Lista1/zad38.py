import string
from functools import reduce
from collections import Counter
import random
import math
import turtle
import datetime

def zad38(str):
    str = str.lower()
    return list(str) == list(reversed(str))
	
print(zad38("okoń"))