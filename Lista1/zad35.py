import string
from functools import reduce
from collections import Counter
import random
import math
import turtle
import datetime

def crypt_impl(str, key):
    squared = list(map(lambda char: key[char] if char in key.keys() else char, str))
    return ''.join(squared)


def crypt(str):
    key = {"a": "y", "e": "i", "i": "o", "o": "a", "y": "e"}
    return crypt(str, key)


def decrypt(str):
    key = {"a": "y", "e": "i", "i": "o", "o": "a", "y": "e"}
    deklucz = {v: k for k, v in key.items()}
    return crypt(str, deklucz)
	
	
c = crypt("qwertyuiopa")
print(decrypt(c))