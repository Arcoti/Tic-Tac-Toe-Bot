import unittest
import numpy as np
from src.backend.model.agent import Agent
from src.backend.ticTacToe.board import Board

class TestAgent(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.bot = Agent(1, self.board)

    def testHorizontalWin(self):
        # Set up board
        board = (0, 1, 1, -1, 0, 0, -1, 0, 0)
        self.board.board = np.array(board).reshape((3, 3))

        # Get Agent action
        actions = self.board.availablePositions()
        state = self.board.getState()
        action = self.bot.chooseAction(state, actions)

        # Test
        expectedMove = (0, 0)
        self.assertEqual(action, expectedMove)
    
    def testVerticalWin(self):
        # Set up board
        board = (1, 0, 0, 0, -1, 0, 1, 0, -1)
        self.board.board = np.array(board).reshape((3, 3))

        # Get Agent action
        actions = self.board.availablePositions()
        state = self.board.getState()
        action = self.bot.chooseAction(state, actions)

        # Test
        expectedMove = (1, 0)
        self.assertEqual(action, expectedMove)

    def testDiagonalWin(self):
        # Set up board
        board = (1, -1, 0, -1, 1, 0, 0, 0, 0)
        self.board.board = np.array(board).reshape((3, 3))

        # Get Agent action
        actions = self.board.availablePositions()
        state = self.board.getState()
        action = self.bot.chooseAction(state, actions)

        # Test
        expectedMove = (2, 2)
        self.assertEqual(action, expectedMove)
    
    def testHorizontalBlock(self):
        # Set up board
        board = (-1, -1, 0, 1, 0, 0, 0, 0, 1)
        self.board.board = np.array(board).reshape((3, 3))

        # Get Agent actions
        actions = self.board.availablePositions()
        state = self.board.getState()
        action = self.bot.chooseAction(state, actions)

        # Test
        expectedMove = (0, 2)
        self.assertEqual(action, expectedMove)

    def testVerticalBlock(self):
        # Set up board
        board = (-1, 1, 0, -1, 0, 1, 0, 0, 0)
        self.board.board = np.array(board).reshape((3, 3))

        # Get Agent actions
        actions = self.board.availablePositions()
        state = self.board.getState()
        action = self.bot.chooseAction(state, actions)

        # Test
        expectedMove = (2, 0)
        self.assertEqual(action, expectedMove)
    
    def testDiagonalBlock(self):
        # Set up board
        board = (-1, 1, 1, 0, -1, 0, 0, 0, 0)
        self.board.board = np.array(board).reshape((3, 3))

        # Get Agent actions
        actions = self.board.availablePositions()
        state = self.board.getState()
        action = self.bot.chooseAction(state, actions)

        # Test
        expectedMove = (2, 2)
        self.assertEqual(action, expectedMove)
    
    def testWinOverBlock(self):
        # Set up board
        board = (0, -1, 1, -1, 0, 1, -1, 1, 0)
        self.board.board = np.array(board).reshape((3, 3))

        # Get Agent actions
        actions = self.board.availablePositions()
        state = self.board.getState()
        action = self.bot.chooseAction(state, actions)

        # Test
        expectedMove = (2, 2)
        self.assertEqual(action, expectedMove)
    
if __name__ == "__main__":
    totalTests = 0
    totalFailures = 0
    totalErrors = 0

    for test in range(100):
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromTestCase(TestAgent)

        runner = unittest.TextTestRunner()
        results = runner.run(suite)

        totalTests += results.testsRun
        totalFailures += len(results.failures)
        totalErrors += len(results.errors)
    
    totalFailed = totalErrors + totalFailures
    failureRate = totalFailed / totalTests if totalTests > 0 else 0

    print(f"Failure Rate: {failureRate: .2%}")
