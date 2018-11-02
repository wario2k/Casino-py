#Player class 
from hand import Hand

class Player():
    def __init__(self,name,score,turn):
        #name of player
        self.name = name
        #player's score
        self.score = score
        #is player turn 
        self.turn = turn 
        #players hand will hold cards 
        self.hand = Hand()
    #accessors/mutators
    def getScore(self):
        return self.score
    def setScore(self,score):
        self.score = score

    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
    
    def getTurn(self):
        self.turn
    def setTurn(self,turn):
        self.turn = turn
        
    def getHand():
        return self.hand