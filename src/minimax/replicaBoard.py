import numpy as np
from ticTacToe.board import Board

class ReplicaBoard(Board):
    def __init__(self, state):
        self.board = np.array(state).reshape((3, 3))
        self.done = False
        self.winner = None
    
    def backStep(self, position):
        # Get the coordinates
        i, j = position

        # Reset the position to empty
        self.board[i][j] = 0
        if self.done:
            self.done = False 
            self.winner = None 

        return self.getState()