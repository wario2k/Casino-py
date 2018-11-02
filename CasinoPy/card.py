class Card():
    def __init__(self, rank, suit):
            self.rank = rank
            self.suit = suit
            if rank == "A":
                    self.isAce = True
    
    def printCard(self):
        return(self.rank + self.suit)
    #get numeric value of card 
    def getValue(self):
        if(self.rank == "A"):
            return(1,14)
        elif(self.rank == "2"):
            return 2
        elif(self.rank == "3"):
            return 3
        elif(self.rank == "4"):
            return 4
        elif(self.rank == "5"):
            return 5
        elif(self.rank == "6"):
            return 6
        elif(self.rank == "7"):
            return 7
        elif(self.rank == "8"):
            return 8
        elif(self.rank == "9"):
            return 9
        elif(self.rank == "X"):
            return 10
        elif(self.rank == "J"):
            return 11
        elif(self.rank == "Q"):
            return 12
        elif(self.rank == "K"):
            return 13        