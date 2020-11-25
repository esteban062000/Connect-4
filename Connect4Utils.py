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
            [Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL,
                Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL],
            [Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL,
                Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL],
            [Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL,
                Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL],
            [Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL,
                Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL],
            [Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL,
                Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL],
            [Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL,
                Constants.EMPTY_VAL, Constants.EMPTY_VAL, Constants.EMPTY_VAL]
        ]
        return gameboard
