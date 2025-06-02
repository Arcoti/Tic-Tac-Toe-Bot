# Tic-Tac-Toe-Bot

## About
This project aims to create a Tic Tac Toe Bot using Reinforcement Learning. 

## Installation and Running the Code

Set up the python virtual environment if this is your first time running the code.
```
python -m venv .venv
```

Set running script to be enabled in your system. 
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Activate the python virtual environment
```
.venv\Scripts\activate
```

Install the python libraries.
```
pip install -r requirements.txt
```

Run the code
```
cd src
python main.py
```

Deactivating the python virtal environment
```
deactivate
```

## Methodology

The Tic Tac Toe Bot is created using Q Learning, with its data stored using a dictionary and application of the Bellman's Equation: 
$$
Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]
$$

The Tic Tac Toe Bot is trained in three stages, playing against itself, playing against a bot implemented using Minimax Algorithm with Alpha Beta Pruning and plyaing against a random bot. The first stage aims to diversify and train the bot against an average player while the second stage aims to train the bot against an excellent player. The last stage aims to diversify the bot data, allowing it to have more varaitions in its model. 

## Acknowledgement

I would like to express my thanks to the following resources:
- [**Reinforcement Learning - Implement Tic Tac Toe**](https://towardsdatascience.com/reinforcement-learning-implement-tictactoe-189582bea542/) and [**Reinforcement Learning Made Simply: Build a Q Learning Agent in Python**](https://towardsdatascience.com/reinforcement-learning-made-simple-build-a-q-learning-agent-in-python/): The articles are used as inspiration and reference for this project
- [**Implement the Minimax Algorithm for AI in python**](https://www.datacamp.com/tutorial/minimax-algorithm-for-ai-in-python): This article helped me to learn the Minimax Algorithm
