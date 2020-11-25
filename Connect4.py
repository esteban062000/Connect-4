from Connect4Utils import Connect4UtilsClass as Utils
import Constants
import random


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
        if (self.computerGoesFirst()):
            players.append(self.player1)
            players.append(self.player2)
        else:
            players.append(self.player2)
            players.append(self.player1)
        while self.getGameResult(self.gameboard) == Constants.GAME_STATE_NOT_ENDED:
            # Se escoje al jugador actual
            activePlayer = players[turnNumber % 2]
            availableMoves = self.getAvailableMoves()
            move = self.getMove(activePlayer, availableMoves)

            turnNumber += 1

    def computerGoesFirst(self):
        return random.randint(0, 1)

    # Devuelve un vector con las tuplas de movimientos legales dado un estado de juego
    def getAvailableMoves(self):
        availableMoves = []
        for j in range(Constants.NUM_COLUMNS):
            if self.gameboard[Constants.NUM_ROWS - 1][j] == Constants.EMPTY_VAL:
                availableMoves.append([Constants.NUM_ROWS - 1, j])
            else:
                for i in range(Constants.NUM_ROWS - 1):
                    if self.gameboard[i][j] == Constants.EMPTY_VAL and self.gameboard[i + 1][j] != Constants.EMPTY_VAL:
                        availableMoves.append([i, j])
        return availableMoves

    def estrategia_M(self, movimientosLegales):
        print("Hola M")
        return 'a'

    def estrategia_H(self, movimientosLegales):
        print("Hola H")
        return 'a'

    def estrategia_R(self, movimientosLegales):
        print("Hola R")
        return 'a'

    # Define cual va a ser el movimiento de un jugador dado el estado de juego y estrategia
    def getMove(self, estrategia, movimientosLegales):
        return getattr(
            self, f"estrategia_{estrategia}", lambda: "Entrada inválida")(movimientosLegales)

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
                while i <= Constants.NUM_ROWS - Constants.REQUIRED_SEQUENCE - 1:
                    if gameboard[i][j] != 0 and gameboard[i][i] == gameboard[i + 1][j + 1] and gameboard[i][i] == gameboard[i + 2][j + 2] and \
                            gameboard[i][i] == gameboard[i + 3][j + 3]:
                        currentWinner = gameboard[i][j]
                        winnerFound = True
                    i = i+1

        if winnerFound:
            return currentWinner
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
