import os
from datetime import datetime
import Constants
import random
import math
import numpy as np


class Connect4UtilsClass:
    def __init__(self, gameId):
        self.id = gameId
        now = datetime.now().strftime("%d-%m-%Y%H%M%S")
        self.fileName = f"./TrainingFiles/{now}{gameId}.txt"

    def createFile(self):
        os.makedirs(os.path.dirname(self.fileName), exist_ok=True)
        f = open(self.fileName, "w")
        f.close()

    def writeFile(self, text):
        f = open(self.fileName, "a")
        f.write(text + '\n')
        f.close()

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

        board = np.zeros((6, 7))
        # return gameboard
        return board

    def copiarTablero(self, gameboard):
        copiaTablero = self.createGameBoard()
        for i in range(Constants.NUM_ROWS):
            for j in range(Constants.NUM_COLUMNS):
                copiaTablero[i][j] = gameboard[i][j]

        return copiaTablero

    def printGameboard(self, activePlayer, gameboard):
        #print(f"\nPlayer {activePlayer} turn")
        # print(np.matrix(gameboard))
        return 0

    def getNextOpenRow(self, board, col):
        for r in range(Constants.NUM_ROWS):
            rowToTry = (Constants.NUM_ROWS - 1) - r
            if board[rowToTry][col] == Constants.EMPTY_VAL:
                return rowToTry

    def drop_piece(self, board, row, col, piece):
        board[row][col] = piece

    '''
    ***************************************************************************************/
    *    Title: MinimaxImplementation
    *    Author: Keith Galli
    *    Date: January, 2019    
    *    Availability: https://github.com/KeithGalli/Connect4-Python
    ***************************************************************************************/
    '''

    def minimax(self, gameboard, depth, alpha, beta, maximizingPlayer):
        AvailableMoves = self.getAvailableMoves(gameboard)
        isTerminalMove = self.is_terminal_node(gameboard)
        if depth == 0 or isTerminalMove:
            # Si el movimiento termina el juego
            if isTerminalMove:
                # Gana el jugador minimax
                if self.winning_move(gameboard, Constants.AI_VAL):
                    return (None, 100000000000000)
                # Gana el oponente
                elif self.winning_move(gameboard, Constants.PLAYER_VAL):
                    return (None, -10000000000000)
                # Empate entre los jugadores
                else:
                    return (None, Constants.GAME_DRAW)
            else:
                return (None, self.score_position(gameboard, Constants.AI_VAL))
        if maximizingPlayer:
            value = -math.inf
            bestcolumn = random.choice(AvailableMoves)
            for col in AvailableMoves:
                row = self.getNextOpenRow(gameboard, col)
                gameboardCopy = self.copiarTablero(gameboard)
                self.drop_piece(gameboardCopy, row, col, Constants.AI_VAL)
                new_score = self.minimax(
                    gameboardCopy, depth - 1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    bestcolumn = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return bestcolumn, value
        else:
            value = math.inf
            bestcolumn = random.choice(AvailableMoves)
            for col in AvailableMoves:
                row = self.getNextOpenRow(gameboard, col)
                gameboardCopy = self.copiarTablero(gameboard)
                self.drop_piece(gameboardCopy, row, col, Constants.PLAYER_VAL)
                new_score = self.minimax(
                    gameboardCopy, depth-1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    bestcolumn = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return bestcolumn, value

    def is_terminal_node(self, gameboard):
        return self.winning_move(gameboard, Constants.AI_VAL) or self.winning_move(gameboard, Constants.PLAYER_VAL) or len(self.getAvailableMoves(gameboard)) == 0

    # Devuelve un vector con las columnas con movimientos disponibles
    def getAvailableMoves(self, gameboard):
        availableMoves = []
        for columna in range(Constants.NUM_COLUMNS):
            if(gameboard[Constants.LAST_AVAILABLE_ROW][columna] == Constants.EMPTY_VAL):
                availableMoves.append(columna)
        return availableMoves

    def winning_move(self, board, piece):
        # Check horizontal locations for win
        for c in range(Constants.NUM_COLUMNS-3):
            for r in range(Constants.NUM_ROWS):
                if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(Constants.NUM_COLUMNS):
            for r in range(Constants.NUM_ROWS-3):
                if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                    return True

        # Check positively sloped diaganols
        for c in range(Constants.NUM_COLUMNS-3):
            for r in range(Constants.NUM_ROWS-3):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                    return True

        # Check negatively sloped diaganols
        for c in range(Constants.NUM_COLUMNS-3):
            for r in range(3, Constants.NUM_ROWS):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                    return True

    def score_position(self, board, piece):  # Este es el scary que hay que arreglar
        # le da un puntaje al board; entre mayor puntaje, mejor es el movimiento
        #print("ENTRO A SCORE POSITION")
        # print(board)
        score = 0

        # Score center column
        center_array = [int(i)
                        for i in list(board[:, Constants.NUM_COLUMNS//2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        # Score Horizontal
        for r in range(Constants.NUM_ROWS):
            row_array = [int(i) for i in list(board[r, :])]
            for c in range(Constants.NUM_COLUMNS-3):
                window = row_array[c:c+Constants.WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        # Score Vertical
        for c in range(Constants.NUM_COLUMNS):
            col_array = [int(i) for i in list(board[:, c])]
            for r in range(Constants.NUM_ROWS-3):
                window = col_array[r:r+Constants.WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        # Score posiive sloped diagonal
        for r in range(Constants.NUM_ROWS-3):
            for c in range(Constants.NUM_COLUMNS-3):
                window = [board[r+i][c+i]
                          for i in range(Constants.WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        for r in range(Constants.NUM_ROWS-3):
            for c in range(Constants.NUM_COLUMNS-3):
                window = [board[r+3-i][c+i]
                          for i in range(Constants.WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        return score

    def evaluate_window(self, window, piece):
        score = 0
        opp_piece = Constants.PLAYER_VAL
        if piece == Constants.PLAYER_VAL:
            opp_piece = Constants.AI_VAL

        if window.count(piece) == 4:
            score += 1000
        elif window.count(piece) == 3 and window.count(Constants.EMPTY_VAL) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(Constants.EMPTY_VAL) == 2:
            score += 2
        if window.count(opp_piece) == 3 and window.count(Constants.EMPTY_VAL) == 1:
            score -= 4

        return score

    def gameboardToTXT(self, gameboard):
        gameboardTXT = ""
        for r in range(len(gameboard)):
            for c in range(len(gameboard[r])):
                value = gameboard[r][c]
                if(value == 0):
                    gameboardTXT += '0'
                elif(value == 1):
                    gameboardTXT += '1'
                elif(value == 2):
                    gameboardTXT += '2'
        return gameboardTXT
