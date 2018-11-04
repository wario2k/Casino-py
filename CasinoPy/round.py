from deck import Deck
from human import Human
from computer import Computer

class Round:
    def __init__(self,num_humanPlayers,num_computerPlayers):
        self.roundNumber = 1

        self.deck = Deck()
        #holds players loaded 
        self.players = []

        self.table = [] 
        
        self.humanPlayernum = num_humanPlayers

        self.num_computerPlayers = num_computerPlayers

# if deck is empty end round
    def isRoundOver(self):
        return if(len(deck) == 0)    
    #load variables from serialization file
    def loadRound():