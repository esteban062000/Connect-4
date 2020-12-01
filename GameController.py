from Connect4 import Connect4 as Connect4Game
from RNA import RNA as NeuralNetwork
import Constants


def main():
    games = int(input("Digite la cantidad de partidas a jugar:\n"))
    if(not isinstance(games, int) or games <= 0):
        print("Valor no aceptado")
        return 0

    function = int(input(
        "Digite 1 para jugar contra la Red Neuronal o 2 para generar material de entrenamiento\n"))
    if(function == 1):
        player = int(input(
            "Digite 3 para jugar Humano vs Red o digite otro valor para jugar Random vs Red\n"))
        if(player == 3):
            model = NeuralNetwork()
            NeuralNetworkWins = 0
            for i in range(games):

                game = Connect4Game(Constants.PLAYER_NETWORK,
                                    Constants.PLAYER_HUMAN, i, model)
                NeuralNetworkWins += game.beginGame()
            print(
                f"La red ha ganado {NeuralNetworkWins} de un total de {games} juegos. Porcentaje de victorias = {NeuralNetworkWins/games}")
        else:
            model = NeuralNetwork()
            NeuralNetworkWins = 0
            for i in range(games):

                game = Connect4Game(Constants.PLAYER_NETWORK,
                                    Constants.PLAYER_RANDOM, i, model)
                NeuralNetworkWins += game.beginGame()
            print(
                f"La red ha ganado {NeuralNetworkWins} de un total de {games} juegos. Porcentaje de victorias = {NeuralNetworkWins/games}")
    else:
        player2 = input("Digite la modalidad de juego de la computadora:\n")
        for i in range(games):
            game = Connect4Game(Constants.PLAYER_MINIMAX, player2, i)
            game.beginGame()

    return 0


if __name__ == "__main__":
    main()
