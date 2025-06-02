from board import Board
from model.agent import Agent

def train(symbol: int, episodes=1000000):
    env = Board()
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
            nextState, reward, done = agent.play(action)

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