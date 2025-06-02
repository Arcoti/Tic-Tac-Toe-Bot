import random
from ticTacToe.board import Board
from model.agent import Agent
from minimax.bot import Bot

class Game:
    def __init__(self):
        self.gameBoard = Board()
        self.player1 = Agent(1, self.gameBoard)
        self.player2 = Bot(-1, self.gameBoard)
    
    def start(self, dataDict):
        done = False
        turn = random.choice([1, -1])

        while not done:
            actions = self.gameBoard.availablePositions()
            state = self.gameBoard.getState()

            if turn == 1:
                action = self.player1.chooseAction(state, actions)
                state, done = self.player1.play(action)

            else:
                action = self.player2.chooseAction(state, actions)
                state, done = self.player2.play(action)
            
            # self.show(state)
            turn *= -1
        
        if self.gameBoard.winner is self.player1:
            print("Winner is Q Learning Agent")
            dataDict["Q Learning Win"] += 1
        elif self.gameBoard.winner is self.player2:
            print("Winner is Minimax Algorithm Bot")
            dataDict["Minimax Win"] += 1
        else:
            print("Game ended in a draw")
            dataDict["Draw"] += 1
        
        return dataDict

    def restart(self):
        self.gameBoard.reset()
            
    def show(self, state):
        for i in range(0, 9, 3):
            print(state[i], state[i + 1], state[i + 2])
        print("-------")