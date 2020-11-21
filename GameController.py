from Connect4 import Connect4 as Connect4Game
import Constants 

def main():
   games = int(input("Digite la cantidad de partidas a jugar:\n"))
   if(not isinstance(games, int) or games <= 0 ):
      print("Valor no aceptado")
      return 0
   
   player2 = input("Digite la modalidad de juego de la computadora:\n")

   for i in range (games):
      game = Connect4Game(Constants.PLAYER_MINIMAX, player2, i)

   return 0



if __name__ == "__main__":
   main()