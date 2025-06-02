import random
from model.trainingBoard import TrainingBoard
from model.agent import Agent
from minimax.bot import Bot
import matplotlib.pyplot as plt

def selfTraining(symbol: int, episodes=100000):
    env = TrainingBoard()
    agent = Agent(symbol, env)
    results = {"win": 0, "draw": 0, "loss": 0}
    winRate, lossRate, drawRate = [], [], []

    for episode in range(episodes):
        state = env.reset()
        done = False
        prev = None

        while not done:
            # Get all available actions
            actions = env.availablePositions()

            # Let agent play the game
            agent.alternateSymbol()
            action = agent.chooseAction(state, actions)
            nextState, reward, done = env.trainingStep(action, agent)

            # Update the agent
            if done:
                if prev is not None:
                    prevState, prevAction, prevReward = prev
                    agent.update(prevState, prevAction, -1 * reward, nextState, [])

                agent.update(state, action, reward, nextState, [])

                # Update Records base on "1" symbol perspective
                if reward == 1 and agent.symbol == 1:
                    results["win"] += 1
                elif reward == 0.5:
                    results["draw"] += 1
                else:
                    results["loss"] += 1

                # Break the loop
                break
        
            if prev is not None:
                prevState, prevAction, prevReward = prev
                nextActions = env.availablePositions()
                agent.update(prevState, prevAction, prevReward, nextState, nextActions)
            
            prev = (state, action, reward)
            state = nextState

        if (episode + 1) % 1000 == 0:
            total = sum(results.values())
            winRate.append(results["win"]/total)
            drawRate.append(results["draw"]/total)
            lossRate.append(results["loss"]/total)

            print(f"Episode {episode + 1}: Wins {results["win"]}, Draws {results['draw']}, Losses {results["loss"]}")
            results = {"win": 0, "draw": 0, "loss": 0}
    
    agent.save()

    return winRate, drawRate, lossRate

def crossTraining(symbol: int, episodes = 1000):
    env = TrainingBoard()
    agent = Agent(symbol, env)
    opponent = Bot(-1 * symbol, env)
    results = {"win": 0, "draw": 0, "loss": 0}
    winRate, lossRate, drawRate = [], [], []

    for episode in range(episodes):
        state = env.reset()
        done = False

        turn = random.choice([1, -1])
        if turn == -1:
            opponentActions = env.availablePositions()
            opponentAction = opponent.chooseAction(state, opponentActions)
            nextState, reward, done = env.trainingStep(opponentAction, opponent)
            state = nextState
        
        while not done:
            actions = env.availablePositions()
            action = agent.chooseAction(state, actions)

            nextState, reward, done = env.trainingStep(action, agent)

            if done:
                agent.update(state, action, reward, nextState, [])

                if reward == 1:
                    results["win"] += 1
                elif reward == 0.5:
                    results["draw"] += 1
                else:
                    results["loss"] += 1

                break
            
            opponentActions = env.availablePositions()
            opponentAction = opponent.chooseAction(nextState, opponentActions)
            nextState2, reward2, done = env.trainingStep(opponentAction, opponent)

            if done:
                agent.update(state, action, -1 * reward2, nextState2, [])

                if reward2 == 1:
                    results["loss"] += 1
                elif reward2 == 0.5:
                    results["draw"] += 1
                else:
                    results["win"] += 1
                
                break
        
            nextActions = env.availablePositions()
            agent.update(state, action, reward, nextState2, nextActions)
            state = nextState2
        
        if (episode + 1) % 100 == 0:
            total = sum(results.values())
            winRate.append(results["win"]/total)
            drawRate.append(results["draw"]/total)
            lossRate.append(results["loss"]/total)

            print(f"Episode {episode + 1}: Wins {results["win"]}, Draws {results['draw']}, Losses {results["loss"]}")
            results = {"win": 0, "draw": 0, "loss": 0}
    
    agent.save()
    
    return winRate, drawRate, lossRate

def show(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print("-------")

def displayTrainingResult(winRate, drawRate, lossRate):
    x = [i * 1000 for i in range(1, len(winRate) + 1)]
    plt.plot(x, winRate, label="Win Rate")
    plt.plot(x, drawRate, label="Draw Rate")
    plt.plot(x, lossRate, label="Loss Rate")
    plt.xlabel("Episodes")
    plt.ylabel("Rate")
    plt.title("Learning Curve of Q Learning Algorithm")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def trainingProcess():
    winRate, drawRate, lossRate = selfTraining(1)              # Symbol is 1 for the agent training
    displayTrainingResult(winRate, drawRate, lossRate)

    winRate, drawRate, lossRate = crossTraining(1)
    displayTrainingResult(winRate, drawRate, lossRate)

if __name__ == "__main__":
    trainingProcess()