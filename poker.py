import math as m
from random import random

class card:
    suit = ''
    value = 0
    id = 0

deck = [None] * 52

def shuffle():
    for x in deck:
        card = random.int(1,52)
        while card not in deck:
            card = random.int(1,52)
        deck[x] = card