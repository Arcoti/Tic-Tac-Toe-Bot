import numpy as np
from ..ticTacToe.board import Board

# Represents the Tic Tac Toe Board
class TrainingBoard(Board):
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.done = False
        self.winner = None
    
    def trainingStep(self, position, player):
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
