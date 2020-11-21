import os
from datetime import datetime

class Connect4:

   def __init__(self, player1, player2, gameIndex):
      '''
      Players: Random, Minimax, Human
      '''
      validPlayers = ['R', 'M', 'H']
      if(player1 in validPlayers and player2 in validPlayers):
         self.player1 = player1
         self.player2 = player2 
      else:
         raise TypeError("Digite un jugador valido")
      
      self.now = datetime.now().strftime("%d-%m-%Y%H%M%S")
      filename = f"./TrainingFiles/{self.now}{gameIndex}.txt"
      os.makedirs(os.path.dirname(filename), exist_ok=True)
      with open(filename, "w") as f:
         f.write("FOOBAR")
