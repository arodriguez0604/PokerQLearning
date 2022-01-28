#SUIT: 0 - Spades, 1 - Diamonds, 2 - Clubs, 3 - Hearts

import math as m
from multiprocessing.sharedctypes import Value
from random import random

#Suit (0-3); Value (1-13)
class Card:
    suit = ''
    value = 0
    id = 0
    
    def __init__(self, suit, value):
        if (suit == 0):
            self.suit = 'S'
        elif (suit == 1):
            self.suit = 'D'
        elif (suit == 2):
            self.suit = 'C'
        elif (suit == 3):
            self.suit = 'H'
        else:
            print ("Error: Bad suit assignment [Poker.py]")

        if (value < 1 or value > 13):
            print ("Error: Bad value assignment [Poker.py]")
                        
        self.value = value

        if (value + (self - 1) * 13 < 1 or value + (self - 1) * 13 > 52):
            print ("Error: Bad id assignment [Poker.py]")

        self.id = value + (self - 1) * 13

    def ChangeID(self, id):
        self.id = id

class Deck:
    deck = [None] * 52

    def __init__(self):
        for x in 4:
            for y in 13:
                self.deck[(13 * x) + y] = Card(x, y + 1)

    def shuffle(self):
        temp[52]

        for i in 52:
            temp[i] = i

        for x in self.deck:
            tempNum = temp[random.int(0, 51 - x)]
            Card.ChangeID(tempNum + 1])
            temp.remove(tempNum)
