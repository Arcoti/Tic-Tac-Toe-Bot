import random
from board import Board
from agent import Agent
from player import Player

def train(symbol: int, episodes=20000):
    env = Board()
    agent = Agent(symbol, env)
    opponent = Player(-1 * symbol, env)
    results = {"win": 0, "draw": 0, "loss": 0}
    winRate, lossRate, drawRate = [], [], []

    for episode in range(episodes):
        state = env.reset()
        done = False

        startFirst = random.randint(0, 1)

        # Opponent Start First
        if startFirst == 0:
            opponentActions = env.availablePositions()
            opponentAction = random.choice(opponentActions)
            nextStateOpp, rewardOpp, done = opponent.play(opponentAction)
            state = nextStateOpp

        while not done:
            # Get all available actions
            actions = env.availablePositions()

            # Let agent play the game 
            # agent.alternateSymbol()
            action = agent.chooseAction(state, actions)
            nextState, reward, done = agent.play(action)

            if done:
                agent.update(state, action, reward, nextState, [])

                # Update Records
                if reward == 1:
                    results["win"] += 1
                elif reward == 0.5:
                    results["draw"] += 1
                else:
                    results["loss"] += 1

                # Break the loop
                break

            opponentActions = env.availablePositions()
            opponentAction = random.choice(opponentActions)
            nextStateOpp, rewardOpp, done = opponent.play(opponentAction)

            if done:
                agent.update(state, action, -1 * rewardOpp, nextStateOpp, [])

                # Update Records
                if rewardOpp == 1:
                    results["loss"] += 1
                elif rewardOpp == 0.5:
                    results["draw"] += 1
                else:
                    results["win"] += 1

                # Break the loop
                break
            
            nextActions = env.availablePositions()
            agent.update(state, action, reward, nextStateOpp, nextActions)
            state = nextStateOpp
            

        if (episode + 1) % 1000 == 0:
            total = sum(results.values())
            winRate.append(results["win"]/total)
            drawRate.append(results["draw"]/total)
            lossRate.append(results["loss"]/total)

            print(f"Episode {episode + 1}: Wins {results["win"]}, Draws {results['draw']}, Losses {results["loss"]}")
            results = {"win": 0, "draw": 0, "loss": 0}
    
    agent.save()

    return winRate, drawRate, lossRate