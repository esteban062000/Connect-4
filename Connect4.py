from Connect4Utils import Connect4UtilsClass as Utils
import Constants
import random
import math


class Connect4:

    def __init__(self, player1, player2, gameIndex):
        '''
        Players: Random, Minimax, Human
        '''
        validPlayers = [Constants.PLAYER_MINIMAX,
                        Constants.PLAYER_HUMAN, Constants.PLAYER_RANDOM]
        if(player1 in validPlayers and player2 in validPlayers):
            self.player1 = player1
            self.player2 = player2
        else:
            raise TypeError("Digite un jugador valido")
        self.utils = Utils(gameIndex)
        self.utils.createFile()
        self.gameboard = self.utils.createGameBoard()

    def beginGame(self):
        turnNumber = 1
        activePlayer = ''
        players = []
        gameover = False
        # self.computerGoesFirst()
        if (True):
            players.append(self.player1)
            players.append(self.player2)
        else:
            players.append(self.player2)
            players.append(self.player1)
        # Mientras haya más de un movimiento disponible

        while len(self.utils.getAvailableMoves(self.gameboard)) > 0 or not gameover:
            # Active player gets chosen and the piece to play on the board is set
            activePlayer = players[turnNumber % 2]
            print(f"Turno de {activePlayer}")
            pieceValue = self.getPieceValue(activePlayer)
            # From our player info we get the collumn chosen
            collumnToPlay = self.getMove(activePlayer)
            AvailableRow = self.utils.getNextOpenRow(
                self.gameboard, collumnToPlay)
            # The piece is placed in the respective collumn
            self.utils.drop_piece(
                self.gameboard, AvailableRow, collumnToPlay, pieceValue)
            # We check the game status in the console
            self.utils.printGameboard(activePlayer, self.gameboard)
            # We check if the game is won or not
            if self.utils.winning_move(self.gameboard, pieceValue):
                gameover = True
            turnNumber += 1

        print(
            f"Player {activePlayer} wins the game in {turnNumber - 1} turns!")

    def getPieceValue(self, activePlayer):
        pieceValue = 0
        if activePlayer == Constants.PLAYER_MINIMAX:
            pieceValue = Constants.AI_VAL
        else:
            pieceValue = Constants.PLAYER_VAL
        return pieceValue

    def computerGoesFirst(self):
        return random.randint(0, 1)

    # Implementa el algoritmo de min max para escoger el mejor movimiento posible dado un estado de juego

    def estrategia_M(self, movimientosLegales):
        col, minimax_score = self.utils.minimax(
            self.gameboard, Constants.MINIMAX_DEPTH, -math.inf, math.inf, True)
        return col

    # Respuesta humana
    def estrategia_H(self, movimientosLegales):
        return movimientosLegales[random.randrange(0, len(movimientosLegales))]

    # Dados los movimientos legales, escoge uno aleatoriamente
    def estrategia_R(self, movimientosLegales):
        return movimientosLegales[random.randrange(0, len(movimientosLegales))]

    # Define cual va a ser el movimiento de un jugador dado el estado de juego y estrategia
    def getMove(self, estrategia):
        availableMoves = self.utils.getAvailableMoves(self.gameboard)
        return getattr(
            self, f"estrategia_{estrategia}", lambda: "Entrada inválida")(availableMoves)
