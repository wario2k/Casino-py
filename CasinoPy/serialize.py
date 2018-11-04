import json
import os

fileName = '/Users/aayushshrestha/Casino OPL python/CasinoPy/serial.txt'
scores = []
hands =[]
piles = []
table =[]
builds = []
deck = []
with open(fileName, mode = 'r') as fh:
    for line in fh:
        #get round number
        if(line.find("Round") != -1):
            roundInfo = " ".join(line.split())
            roundInfo = roundInfo.split()
        elif(line.find("Score:") != -1):
            scoreInfo =" ".join(line.split())
            scoreInfo = scoreInfo.split()
            scores.append(scoreInfo)
        elif(line.find("Hand:") != -1):
            handInfo =" ".join(line.split())    
            handInfo = handInfo.split()
            hands.append(handInfo)
        elif(line.find("Pile:") != -1):
            pileInfo = " ".join(line.split())
            pileInfo = pileInfo.split()
            piles.append(pileInfo)
        elif(line.find("Table:") != -1):
            tableInfo = " ".join(line.split())
            tableInfo = tableInfo.split()
            table.append(tableInfo)
        elif(line.find("Build Owner:") != -1):
            buildInfo = " ".join(line.split())
            buildInfo = buildInfo.split(":")
            buildInfo = buildInfo[1].split()
            builds.append(buildInfo)
        elif(line.find("Deck: ") != -1):
            _deck = " ".join(line.split())
            _deck = _deck.split()
            deck.append(_deck)
        elif(line.find("Next Player: ") != -1):
            nextPlayer = " ".join(line.split())
            nextPlayer = nextPlayer.split()

#get respective scores
roundNumber = roundInfo[1]
computerScore = scores[0][1]
humanScore = scores[1][1]

#get computer and human hands 
computerHand = [x for x in hands[0] if x != "Hand:"]
humanHand = [x for x in hands[1] if x != "Hand:"]
#get computer and human piles 
computerPile = [x for x in piles[0] if x != "Pile:"]
humanPile = [x for x in piles[1] if x != "Pile:"]
#get table cards
tableCards = [x for x in table[0] if x != "Table:"]
deck = [x for x in deck[0] if x != "Deck:"]
#get next player
nextPlayer = nextPlayer[2]

print(nextPlayer)

