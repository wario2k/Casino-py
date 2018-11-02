class Hand:
    def __init__(self):
        #holds cards in hand 
        self.hand = []
    #sets player hand
    def setHand(self,hand):
        self.hand = hand
    #checks if card is in hand
    def cardInHand(self,card):
        return card in self.hand
    #play card from hand 
    def playCard(self,card):            
        self.hand.remove(card)
    #adds card to hand 
    def addCard(self,card):
        self.hand.append(card)
    def getHandSize(self):
        return len(self.hand)
    #check if hand is empty
    def checkHandEmpty(self):
        return len(self.hand) == 0     

    #return list of cards in hand 
    def getHandCardList(self):
        return self.hand[:]        