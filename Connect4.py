from Connect4Utils import Connect4UtilsClass as Utils
import Constants 

class Connect4:

   def __init__(self, player1, player2, gameIndex):
      '''
      Players: Random, Minimax, Human
      '''
      validPlayers = [Constants.PLAYER_MINIMAX, Constants.PLAYER_HUMAN, Constants.PLAYER_RANDOM]
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
      if (self.utils.computerGoesFirst()):
         players.append(self.player1)
         players.append(self.player2)
      else:
         players.append(self.player2)
         players.append(self.player1)
      while self.utils.getGameResult(self.gameboard) == Constants.GAME_STATE_NOT_ENDED:
         activePlayer = players[turnNumber % 2]
         turnNumber += 1
   