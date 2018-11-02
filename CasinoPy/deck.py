'''
Deck class creates and shuffels deck 
'''
import random
from card import Card
suits = ["S","D","H","C"]
ranks = ["A","2","3","4","5","6","7","8","9","X","J","Q","K"]
class Deck():
    def __init__(self):
            self.remaining = [] #what cards are left, haven't been dealt yet
            for s in suits: #populating the deck with 52 cards
                    for rank in ranks:
                            self.remaining.append(Card(rank, s))
            self.played = [] #what cards have already been played

    def shuffle(self):
            random.shuffle(self.remaining)

    def draw(self):
            if self.count() == 0:
                    return "Sorry, your deck is empty, there are no cards to be drawn." #this shouldn't happen in Casino
            drawnCard = self.remaining.pop() #draw a card, taking it out of the list of remaining cards
            self.played.append(drawnCard) #and put it into the list of already played cards
            return drawnCard

    def count(self): #if you wanted to know how many cards were left (also not used in Casino)
            return len(self.remaining)
    
    def printDeck(self):
        for x in self.remaining:
            print(x.printCard())

#Description : Loading deck from serialization file 
#Input : serializedDeck -> list of cards read from serialization file
    def loadDeck(self, serializedDeck):
        for card in serializedDeck:
            self.remaining.append(card)