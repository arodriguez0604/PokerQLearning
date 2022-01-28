#SUIT: 0 - Spades, 1 - Diamonds, 2 - Clubs, 3 - Hearts

import math as m
from multiprocessing.sharedctypes import Value
from random import random

class Card:
    suit = ''
    value = 0
    
    def __init__(self, suit, value):
        if (suit == 1):
            self.suit = 'S'
        elif (suit == 2):
            self.suit = 'D'
        elif (suit == 3):
            self.suit = 'C'
        elif (suit == 4):
            self.suit = 'H'
        else:
            print ("Error: Bad suit assignment [Poker.py]")

        if (value < 1 or value > 13):
            print ("Error: Bad value assignment [Poker.py]")
                        
        self.value = value
    
    def getSuit():
        return self.suit

    def getValue():
        return value




deck = [None] * 52

def createDeck():
    for x in 4:
        for y in 13:
            deck[x][y] = Card(x, y)

def shuffle():
    for x in deck:

    random.int()
