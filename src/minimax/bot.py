from ticTacToe.player import Player
from minimax.replicaBoard import ReplicaBoard

# Minimax Algorithm Bot
class Bot(Player):
    def __init__(self, symbol, game):
        super().__init__(symbol, game)
        self.imaginaryOpponent = Player(-1 if symbol == 1 else 1, game)

    def chooseAction(self, state, actions):
        # Create a replica of the board
        # Step and backstep will not affect actual game
        replicaBoard = ReplicaBoard(state)

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

    # Alpha and Beta for Alpha Beta Pruning
    # Alpha is Best Max so Far
    # Beta is Best Min so Far
    def minimax(self, replicaBoard: ReplicaBoard, depth: int, maximising: bool, alpha = float('-inf'), beta = float('inf')):
        # Terminating Condition
        if replicaBoard.done is True:
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
                score = self.minimax(replicaBoard, depth + 1, False, alpha, beta)
                replicaBoard.backStep(action)

                # Bot will maximise the score for itself
                bestScore = max(score, bestScore)
                alpha = max(score, alpha)

                if beta <= alpha:
                    break # Prune
                
            return bestScore
        # Opponent's Turn
        else:
            bestScore = float('inf')

            actions = replicaBoard.availablePositions()

            for action in actions:
                replicaBoard.step(action, self.imaginaryOpponent)
                score = self.minimax(replicaBoard, depth + 1, True, alpha, beta)
                replicaBoard.backStep(action)

                # Opponent will minimise the score for Bot
                bestScore = min(score, bestScore)
                beta = min(score, beta)

                if beta <= alpha:
                    break # Prune

            return bestScore
                