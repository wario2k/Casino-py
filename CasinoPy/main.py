from deck import Deck
from card import Card
import os

#temp holders for loaded game
computerScore = 0
humanScore = 0
loadedRound = 0
computerHand = []
computerPile = []
humanHand = []
humanPile = []
scores = []
hands =[]
piles = []
tableCards = []
table =[]
builds = []
deck = []
#start main game 
#load round
    #load players
    #load deck
    #load hands 
#start round 
    #new round
#initialize players 


#Description : This function displays initial menu for tournament and asks for user selection
#parameters : none
#returns : deck, builds , computerScore, humanScore,loadedRound, computerHand, humanHand, tableCards, computerPile, humanPile, nextPlayer
#           all values read from the serialzation file for 2 players 
#           only handles input for two players 

def mainMenuSelection():
    print("Welcome to Casino!")
    print("Please select what you would like to do:")
    print("1. Start new game")
    print("2. Load game from file")
    user_input = -1 
    while(user_input < 0 or user_input > 2):
        user_input = int(input("Please select what you would like to do: "))

    return user_input

#Description : Loads values for serialization from text file
#Parameters : deck -> list of cards builds -> list holding all builds for tables
#returns : all values required for getting game state
def loadNewGame(deck = deck, builds = builds):
    file_name = str(input("Please select file you would like to load from: "))
    if os.path.exists(file_name):
        with open(file_name, mode = 'r') as fh:
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
    else:
        print("The file you are trying to load from does not exist! Game will now exit.")
        exit(0)

    #get round number
    loadedRound = roundInfo[1]
    #get respective scores
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
    return(deck, builds , computerScore, humanScore,loadedRound, computerHand, humanHand, tableCards, computerPile, humanPile,nextPlayer)

#loading decks

#Description starts tournament 
def startTournament():
    #asks user to select whether to start new game or load game from file
    userSelected = mainMenuSelection()
    if(userSelected == 1):
        print("Start new game!")
        #get number of players 
        while(1):
            humanPlayers = int(input("How many human players would like to play: "))
            cpuPlayers = int(input("How many computer players would like to play: "))
            total = humanPlayers + cpuPlayers
            if(total > 0 and total < 5 ):
                print("Okay! Starting the game with ", humanPlayers, " human players and", cpuPlayers, "computer players.")
                break
            else:
                print("Invalid number of players!")

        load_deck = loadDeck()
        if(load_deck == 1):
            print("Starting new round with everything new initalized!")
            #beginNewRound()
        #load deck from file specified 
        else:
           new_cards =  loadCards()
        #beginNewRound()
    else:
    #load new game    
        deck, builds , computerScore, humanScore,loadedRound, computerHand, humanHand, tableCards, computerPile, humanPile, nextPlayer = loadNewGame()
        print("Loaded files from new game")

def loadCards():
    filename = input("Please enter name of file to load deck from : ")
    deck = Deck()
    cards = []
    if(os.path.exists(filename)):
        deck.emptyDeck()
        
        with open(filename, mode = 'r') as fh:
            for line in fh:
                cards.append(line)
        
        deck.loadDeck(cards)
        deck.printDeck()
        return deck
        
    else:
        print("No cards were found loading a new deck instead")
        return deck        
def loadDeck():
    print("Where do you want to load the deck from:")
    print("1. Load random deck")
    print("2. Load preset deck")
    
    while(1):
        x = int(input("Make a selection: "))
        if(x == 1 or x ==2 ):
            return x
        else:
            print("Invalid selection!")    
    #function to display new round
startTournament()