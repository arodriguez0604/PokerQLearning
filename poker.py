from ast import Try
from cgitb import reset
import random

#Suit (0-3); Value (1-13)
class Card:
    suit = ''
    value = 0
    
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

        if (value + suit * 13 < 1 or value + suit * 13 > 52):
            print ("Error: Bad id assignment [Poker.py]")
    
    def setValue(self, value):
        self.value = value
    
    def getValue(self):
        return self.value

    def setSuit(self, suit):
        self.suit = suit
    
    def getSuit(self):
        return self.suit

    def display(self):
        print ("{}{}".format(self.value, self.suit))


class Deck:

    def __init__(self):
        self.deck = []
        for x in range(4):
            for y in range(13):
                self.deck.append(Card(x, y + 1))

    def shuffle(self):
        for i in range (51, -1, -1):
            r = random.randint(0, i)
            self.deck[r], self.deck[i] = self.deck[i], self.deck[r] 
        
    #returns a card
    def drawCard(self):
        return self.deck.pop(0)

    def display(self):
        for i in self.deck:
            i.display()

class Group:
    hand = []
    cards = 0

    def __init__(self):
        self.hand = []

    def __init__(self, deck, card):
        self.cards = card
        for k in range(self.cards):
            self.hand.append(deck.drawCard())
        if not self.hand:
            print ("Error: Bad Hand Allocation [Pokey.py]")
        
    def newHand(self, deck):
        try:
            for i in range(self.cards):
                self.hand.pop(0)
        except:
            print ("Error: Bad Hand Removal [Poker.py]")

        for k in range(self.cards):
            self.hand.append(deck.drawCard())
        
        if not self.hand:
            print ("Error: Bad Hand Allocation [Pokey.py]")

    def getHand(self):
        return self.hand
    
    def displayHand(self):
        for i in self.hand:
            i.display()

        


#Start of main function
deck = Deck()
deck.shuffle()
deck.display()
player1 = Group(deck, 2)
print ("\n\n\nHAND:")
player1.displayHand()