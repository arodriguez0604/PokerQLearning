from ast import Try
from cgitb import reset
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

        if (value + suit * 13 < 1 or value + suit * 13 > 52):
            print ("Error: Bad id assignment [Poker.py]")

        self.id = value + suit * 13

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
        for x in range(4):
            for y in range(13):
                self.deck.append(Card(x, y + 1))

    def shuffle(self):
        for i in range (51, -1, -1):
            r = random.randint(0, i)
            temp = self.deck[i]
            self.deck[i] = self.deck[r]
            self.deck[r] = temp
        
    #returns a card
    def drawCard(self):
        return self.deck.pop(len(self.deck) - 1)

    def display(self):
        for i in self.deck:
            print(self.deck[i].getValue()+self.deck[i].getSuit()+" ")    


class Hand:
    hand = []

    def __init__(self):
        self.hand = []

    def __init__(self, card1, card2):
        self.hand.append(card1)
        self.hand.append(card2)

        if not self.hand:
            print ("Error: Bad Hand Allocation [Pokey.py]")   

    def __init__(self, card1, card2, card3):
        self.hand.append(card1)
        self.hand.append(card2)
        self.hand.append(card3)

        if not self.hand:
            print ("Error: Bad Hand Allocation [Pokey.py]")  

    def getHand(self):
        return self.hand

    def newHand(self, deck):
        try:
            self.hand.pop(len(self.hand) - 1)
            self.hand.pop(len(self.hand) - 1)
        except:
            print ("Error: Bad Hand Removal [Poker.py]")
        
        if (len(self.hand) != 0):
            print ("Error: Bad Hand Removal [Poker.py]")

        self.hand.append(deck.drawCard())
        self.hand.append(deck.drawCard())

        if not self.hand:
            print ("Error: Bad Hand Allocation [Pokey.py]")

#Start of main function
deck = Deck()
deck.shuffle()
for i in range(52):
    deck.display()