import time
import pygame
import sys
from .ticTacToe.game import interactiveGame, simulationGame

if __name__ == "__main__":
    choice = None
    running = True

    while True:
        choice = input("Do you want to play with the agent? (y/n): ")
        if choice.lower() == 'y' or choice.lower() == 'n':
            break
        else:
            print("Invalid input choice. Please input again.")

    if choice.lower() == 'y':
        interactiveGame()
    else:
        simulationGame()