from ticTacToe.player import Player
from replicaBoard import ReplicaBoard

class Bot(Player):
    def __init__(self, symbol, game):
        super().__init__(symbol, game)
        self.imaginaryOpponent = Player(-1 if symbol == 1 else 1, game)

    def chooseAction(self, board):
        # Create a replica of the board
        # Step and backstep will not affect actual game
        replicaBoard = ReplicaBoard(board)

        # Get avaialble actions
        actions = replicaBoard.availablePositions()

        # Intialize best action and score
        bestAction = None
        bestScore = float('-inf')

        # Loop through the action
        for action in actions:
            replicaBoard.step(action, self)
            score = self.minimax(replicaBoard, 0, False)
            replicaBoard.backStep(action)

            # Update action accordingly
            if score > bestScore:
                bestAction = action
                bestScore = score
        
        # Return the best action
        return bestAction

    def minimax(self, replicaBoard: ReplicaBoard, depth: int, maximising: bool):
        # Terminating Condition
        if replicaBoard.done:
            if replicaBoard.winner is self:
                return +1
            elif replicaBoard.winner is None:
                return 0
            else:
                return -1
        
        # Bot's Turn
        if maximising:
            bestScore = float('-inf')

            actions = replicaBoard.availablePositions()

            for action in actions:
                replicaBoard.step(action, self)
                score = self.minimax(replicaBoard, depth + 1, False)
                replicaBoard.backStep(action)

                # Bot will maximise the score for itself
                bestScore = max(score, bestScore)
                
            return bestScore
        # Opponent's Turn
        else:
            bestScore = float('inf')

            actions = replicaBoard.availablePositions()

            for action in actions:
                replicaBoard.step(action, self.imaginaryOpponent)
                score = self.minimax(replicaBoard, depth + 1, True)
                replicaBoard.backStep(action)

                # Opponent will minimise the score for Bot
                bestScore = min(score, bestScore)

            return bestScore
                