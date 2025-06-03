import unittest
import numpy as np
from src.backend.ticTacToe.board import Board
from src.backend.ticTacToe.player import Player

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.testPlayer = Player(1, self.board)

    def testHorizontalWin(self):
        # Set up board
        board = (0, 1, 1, -1, 0, 0, -1, 0, 0)
        self.board.board = np.array(board).reshape((3, 3))

        # Make a move
        self.testPlayer.play((0, 0))

        # Test
        expectedDone = True
        expectedWinner = self.testPlayer
        self.assertEqual(expectedDone, self.board.done)
        self.assertEqual(expectedWinner, self.board.winner)

    def testVerticalWin(self):
        # Set up board
        board = (1, 0, 0, 0, -1, 0, 1, 0, -1)
        self.board.board = np.array(board).reshape((3, 3))

        # Make a move
        self.testPlayer.play((1, 0))
    
        # Test
        expectedDone = True
        expectedWinner = self.testPlayer
        self.assertEqual(expectedDone, self.board.done)
        self.assertEqual(expectedWinner, self.board.winner)

    def testDiagonalWin(self):
        # Set up board
        board = (1, -1, 0, -1, 1, 0, 0, 0, 0)
        self.board.board = np.array(board).reshape((3, 3))

        # Make a move
        self.testPlayer.play((2, 2))

        # Test
        expectedDone = True
        expectedWinner = self.testPlayer
        self.assertEqual(expectedDone, self.board.done)
        self.assertEqual(expectedWinner, self.board.winner)

    def testDraw(self):
        # Set up board
        board = (1, -1, 1, -1, -1, 1, -1, 0, -1)
        self.board.board = np.array(board).reshape((3, 3))

        # Make a move
        self.testPlayer.play((2, 1))

        # Test
        expectedDone = True
        expectedWinner = None
        self.assertEqual(expectedDone, self.board.done)
        self.assertEqual(expectedWinner, self.board.winner)

        # Reset
        self.board.done = False
        self.board.winner = None
    
    def testContinue(self):
        # Set up board
        board = (1, -1, 0, 0, 0, 0, 0, 0, 0)
        self.board.board = np.array(board).reshape((3, 3))

        # Move
        self.testPlayer.play((0, 2))

        # Test
        expectedDone = False
        expectedWinner = None
        self.assertEqual(expectedDone, self.board.done)
        self.assertEqual(expectedWinner, self.board.winner)

if __name__ == "__main__":
    unittest.main()