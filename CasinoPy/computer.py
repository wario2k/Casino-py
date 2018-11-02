
from player import Player

class Computer(Player):
    #constructor for computer class 
	def __init__(self, name, score, turn):
		super().__init__(name,score,turn)