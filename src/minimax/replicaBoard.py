from ticTacToe.board import Board

class ReplicaBoard(Board):
    def __init__(self, board: Board):
        self.board = board.board.copy()
        self.done = board.done
        self.winner = board.winner
    
    def backStep(self, position):
        # Get the coordinates
        i, j = position

        # Reset the position to empty
        self.board[i][j] = 0

        return self.getState()