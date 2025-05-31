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
    
    def step(self, position: tuple[int, int], player: Player):
        # Check if the game is over
        if self.done:
            raise ValueError("Game Over")
        
        # Get the coordinates
        i, j = position

        # If place on an non-empty position in the board, penalise the machine
        # Return True to signal that the game has ended
        if self.board[i][j] != 0:
            return self.getState(), -10, True
        
        # Mark the player move on the board
        self.board[i][j] = player.symbol

        # Check if the player won, and reward them with 1 if they won 
        # Return True to signal that the game has ended
        if self.checkWinner(player):
            self.done = True
            self.winner = player
            return self.getState(), 1, True
    
        # Check if the game has ended in a draw, and reward them with 0.5 if draw
        # Return True to signal that the game has ended
        elif not self.availablePositions():
            self.done = True
            return self.getState(), 0.5, True
    
        # Default
        # Return False to signal that the game has not end
        return self.getState(), 0, False
