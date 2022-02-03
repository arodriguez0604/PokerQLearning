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

class Group:
    cardNum = 0
    def __init__(self, cardTempNum):
        cardNum = cardTempNum
        self.resetHand()

    def resetHand():
        hand = []
    
    def addCard(self, card):
        self.hand.append(card)
        # maybe add a check for no duplicates?

    def removeCard(self, card):
        self.hand.remove(self.hand.index(card))
        # maybe add a check to only remove if the card exists
        
    def displayCards(self):
        for x in self.hand:
            print (self.hand[x])

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

class Player:
    hand = []
    river = False

    def __init__(self, deck, river):
        for i in range(2):
            self.hand.append(deck.drawCard())
        
        if (river == True):
            self.river = True
            self.hand.append(deck.drawCard())

        if not self.hand:
            print ("Error: Bad Hand Allocation [Pokey.py]")   

    def getHand(self):
        return self.hand

    def newHand(self, deck):
        try:
            for i in range(2):
                self.hand.pop(len(self.hand) - 1)
            if (self.river):
                for j in range(3):
                    self.hand.pop(len(self.hand) - 1)

        except:
            print ("Error: Bad Hand Removal [Poker.py]")
        
        if (len(self.hand) != 0):
            print ("Error: Bad Hand Removal [Poker.py]")

        for k in range(2):
            self.hand.append(deck.drawCard())
        if (self.river):
            self.hand.append(deck.drawCard())

        if not self.hand:
            print ("Error: Bad Hand Allocation [Pokey.py]")
        
    def addCard(self, deck):
        if (self.river):
            self.hand.append(deck.drawCard())
        


#Start of main function
deck = Deck()
deck.shuffle()

player1 = Player(deck, True)
hand = player1.getHand()

for i in range(len(hand)):
    print(hand[i].getID())
