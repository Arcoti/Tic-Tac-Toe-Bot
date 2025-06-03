from collections import defaultdict
import random
import pickle
from ..ticTacToe.player import Player
from ..ticTacToe.board import Board

# Q Learning Agent
class Agent(Player):
    def __init__(self, symbol: int, game: Board, alpha = 0.1, gamma = 0.9, epsilon = 0.1):
        super().__init__(symbol, game)
        self.Q = self.load()     
        self.alpha = alpha              # Learning Rate (Weight given to new information)
        self.gamma = gamma              # Discount Factor (Importance of Future Reward)
        self.epsilon = epsilon          # Exploration Probability
    
    # Get the q value 
    def getQ(self, state, action):
        return self.Q[(state, action)]
    
    # Let the agent perform an action
    def chooseAction(self, state, actions):
        if random.random() < self.epsilon:
            # Explore actions
            return random.choice(actions)
        else:
            # Choose the best actions
            qValues = [self.getQ(state, action) for action in actions]
            maxQ = max(qValues)
            bestActions = [action for action, q in zip(actions, qValues) if q == maxQ]
            return random.choice(bestActions)
    
    # Update q value base on future rewards
    def update(self, state, action, reward, nextState, nextActions):
        nextMaxQ = max([self.getQ(nextState, action) for action in nextActions], default = 0)
        oldValue = self.Q[(state, action)]  
        # Bellman Equation
        newValue = oldValue + self.alpha * (reward + self.gamma * nextMaxQ - oldValue)
        self.Q[(state, action)] = newValue
    
    # Save the model using pickle 
    def save(self):
        with open('./src/model/qTable.pkl', 'wb') as file:
            pickle.dump(self.Q, file)
    
    # Load the model if the file exist else start a brand new Q table
    def load(self):
        try:
            with open('./src/model/qTable.pkl', 'rb') as file:
                print("Load Q Table from file")
                return pickle.load(file)
        except FileNotFoundError:
            print("No Q Table found. Starting a new one.")
            return defaultdict(float) # Dictionary with key as (state, action) and value as q value; Returns 0.0 when key is missing
