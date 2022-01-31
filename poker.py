import random

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

    def setID(self, id):
        self.id = id

    def getID(self):
        return self.id
    
    def setValue(self, value):
        self.value = value
    
    def getValue(self):
        return self.value

    def setSuit(self, suit):
        self.suit = suit
    
    def getSuit(self):
        return self.suit


class Deck:

    def __init__(self):
        self.deck = []
        for x in 4:
            for y in 13:
                self.deck.append(Card(x, y + 1))

    def shuffle(self):
        for i in range (1,52,1):
            r = random.randint(0,52)
            self.deck[i], self.deck[r] = self.deck[r], self.deck[i]

class Hand:
    hand = []

    def __init__(self, card1, card2):
        self.hand.append(card1)
        self.hand.append(card2)