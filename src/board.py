import numpy as np
from player import Player

# Represents the Tic Tac Toe Board
class Board:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.done = False
        self.winner = None
    
    # Reset the board to the original state
    def reset(self):
        self.board[:] = 0
        self.done = False
        self.winner = None
        return self.getState()
    
    # Return the state of the board as a 1-dimensional array
    def getState(self):
        return tuple(self.board.flatten())
    
    # Return the coordinates where has not been taken or placed by players yet
    def availablePositions(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == 0]
    
    # Check if the input player won
    def checkWinner(self, player: Player):
        for i in range(3):
            # Check whether all elements in the horizontal or vertical row is equal to the player symbol
            if all(self.board[i, :] == player.symbol) or all(self.board[: , i] == player.symbol):
                return True
            # Check whether all elements in the diagonal or flip horizontally array is equal to player symbol
            elif all(np.diag(self.board) == player.symbol) or all(np.diag(np.fliplr(self.board)) == player.symbol):
                return True
    
    def play(self, position: tuple, player: Player):
        pass