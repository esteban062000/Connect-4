import os
from datetime import datetime
import Constants 
import random
'''
***************************************************************************************/
*    Title: Connect 4 source code
*    Author: Marius Borcan
*    Date: April, 2020    
*    Availability: https://github.com/bdmarius/nn-connect4
*
***************************************************************************************/
'''

class Connect4UtilsClass:
    def __init__(self, gameId):
        self.id = gameId
        now = datetime.now().strftime("%d-%m-%Y%H%M%S")
        self.fileName = f"./TrainingFiles/{now}{gameId}.txt"
    
    def createFile(self):
        os.makedirs(os.path.dirname(self.fileName), exist_ok=True)
        f = open(self.fileName, "w")
        f.close() 

    def writeFile(self, currentGameState, moveDone):
        raise NotImplementedError

    def createGameBoard(self):
        gameboard = [
            [Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL],
            [Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL],
            [Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL],
            [Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL],
            [Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL],
            [Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL]
        ]
        return gameboard
    
    # Returns a number in range [0, 1]
    def computerGoesFirst(self):
        return random.randint(0, 1)

    def getAvailableMoves(self, gameboard):
        availableMoves = []
        for j in range(Constants.NUM_COLUMNS):
            if gameboard[Constants.NUM_ROWS - 1][j] == Constants.EMPTY_VAL:
                availableMoves.append([Constants.NUM_ROWS - 1, j])
            else:
                for i in range(Constants.NUM_ROWS - 1):
                    if gameboard[i][j] == Constants.EMPTY_VAL and gameboard[i + 1][j] != Constants.EMPTY_VAL:
                        availableMoves.append([i, j])
        return availableMoves

    def getGameResult(self, gameboard):
        winnerFound = False
        currentWinner = None
        # Find winner on horizontal
        for i in range(Constants.NUM_ROWS):
            if not winnerFound:
                for j in range(Constants.NUM_COLUMNS - Constants.REQUIRED_SEQUENCE - 1):
                    if gameboard[i][j] != 0 and gameboard[i][j] == gameboard[i][j+1] and gameboard[i][j] == gameboard[i][j + 2] and \
                            gameboard[i][j] == gameboard[i][j + 3]:
                        currentWinner = gameboard[i][j]
                        winnerFound = True

        # Find winner on vertical
        if not winnerFound:
            for j in range(Constants.NUM_COLUMNS):
                if not winnerFound:
                    for i in range(Constants.NUM_ROWS - Constants.REQUIRED_SEQUENCE - 1):
                        if gameboard[i][j] != 0 and gameboard[i][j] == gameboard[i+1][j] and gameboard[i][j] == gameboard[i+2][j] and \
                                gameboard[i][j] == gameboard[i+3][j]:
                            currentWinner = gameboard[i][j]
                            winnerFound = True

        # Check lower left diagonals
        if not winnerFound:
            for i in range(Constants.NUM_ROWS - Constants.REQUIRED_SEQUENCE - 1):
               j = 0
               while j <= i:
                   if gameboard[i][j] != 0 and gameboard[i][i] == gameboard[i + 1][j + 1] and gameboard[i][i] == gameboard[i + 2][j + 2] and \
                           gameboard[i][i] == gameboard[i + 3][j + 3]:
                       currentWinner = gameboard[i][j]
                       winnerFound = True
                   j = j+1

        # Check upper right diagonals
        if not winnerFound:
            for j in range(Constants.NUM_COLUMNS - Constants.REQUIRED_SEQUENCE - 1):
                i = j
                while i<= Constants.NUM_ROWS - Constants.REQUIRED_SEQUENCE - 1:
                    if gameboard[i][j] != 0 and gameboard[i][i] == gameboard[i + 1][j + 1] and gameboard[i][i] == gameboard[i + 2][j + 2] and \
                            gameboard[i][i] == gameboard[i + 3][j + 3]:
                        currentWinner = gameboard[i][j]
                        winnerFound = True
                    i = i+1

        if winnerFound: return currentWinner
        else:
            drawFound = True
            # Check for draw
            for i in range(len(gameboard)):
                for j in range(len(gameboard[i])):
                    if gameboard[i][j] == Constants.EMPTY_VAL:
                        drawFound = False
            if drawFound:
                return Constants.GAME_STATE_DRAW
            else:
                return Constants.GAME_STATE_NOT_ENDED