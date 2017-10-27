import string
from functools import reduce
from collections import Counter
import random
import math
import turtle
import datetime

def zad36(str):
    return not (set(string.ascii_lowercase).difference(set(str.lower())))
	
zad36()