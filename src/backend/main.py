from .ticTacToe.game import Game

def main():
    game = Game()
    dataDict = {"Q Learning Win": 0, "Minimax Win": 0, "Draw": 0}

    for i in range(10):
        dataDict = game.start(dataDict)
        game.restart()

        if (i + 1) % 100 == 0:
            print(dataDict)

if __name__ == "__main__":
    main()