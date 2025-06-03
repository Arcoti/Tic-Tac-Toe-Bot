import random
import sys
import pygame
import time

from .player import Player
from .board import Board
from ..model.agent import Agent
from ..minimax.bot import Bot


# Constants
WIDTH, HEIGHT = 300, 300
LINEWIDTH = 5
BOARDROWS, BOARDCOLS = 3, 3
SQUARESIZE = WIDTH // BOARDCOLS
CIRCLERADIUS = SQUARESIZE // 3
CIRCLEWIDTH = 15
CROSSWIDTH = 25
SPACE = SQUARESIZE // 4

# Colours
WHITE, BLACK = (255, 255, 255), (0, 0, 0)

def drawLines(screen):
    # horizontal
    pygame.draw.line(screen, BLACK, (0, SQUARESIZE), (WIDTH, SQUARESIZE), LINEWIDTH)
    pygame.draw.line(screen, BLACK, (0, 2* SQUARESIZE), (WIDTH, 2 * SQUARESIZE), LINEWIDTH)

    # verticle
    pygame.draw.line(screen, BLACK, (SQUARESIZE, 0), (SQUARESIZE, HEIGHT), LINEWIDTH)
    pygame.draw.line(screen, BLACK, (2 * SQUARESIZE, 0), (2 * SQUARESIZE, HEIGHT), LINEWIDTH)

def drawSymbols(symbol, row, col, screen):
    if symbol == 1:
        # Draw X
        pygame.draw.line(screen, BLACK, 
                         (col * SQUARESIZE + SPACE, row * SQUARESIZE + SPACE),
                         (col * SQUARESIZE + SQUARESIZE - SPACE, row * SQUARESIZE + SQUARESIZE - SPACE),
                         CROSSWIDTH)
        pygame.draw.line(screen, BLACK, 
                         (col * SQUARESIZE + SPACE, row * SQUARESIZE + SQUARESIZE - SPACE), 
                         (col * SQUARESIZE + SQUARESIZE - SPACE, row * SQUARESIZE + SPACE), 
                         CROSSWIDTH)
    elif symbol == -1:
        # Draw O
        pygame.draw.circle(screen, BLACK, 
                            (col * SQUARESIZE + SQUARESIZE // 2, row * SQUARESIZE + SQUARESIZE // 2), 
                            CIRCLERADIUS, 
                            CIRCLEWIDTH)

def drawBoard(state, screen):
    for row in range(0, 9, 3):
        for col in range(3):
            drawSymbols(state[row + col], row // 3, col, screen)
    
    pygame.display.update()

def drawEndMessage(text, fontSize, screen):
    font = pygame.font.SysFont(None, fontSize)
    textSurface = font.render(text, True, BLACK) # Render text surface

    # Generate text surface base on text dimensions
    rect = textSurface.get_rect(center = (WIDTH/2, HEIGHT/2)) 

    screen.fill(WHITE)

    # Blit the textSurface on to he screen using rect dimensions, and update it
    screen.blit(textSurface, rect)
    pygame.display.update()

def restart(screen, gameBoard): 
    # Reset the entire game
    screen.fill(WHITE)
    gameBoard.reset()
    drawLines(screen)
    return True, False

def interactiveGame():
    # Initialize
    pygame.init()
    gameBoard = Board()
    agent = Agent(1, gameBoard)
    player = Player(-1, gameBoard)

    # Variables
    turn = random.choice([1, -1])
    first = True

    # Screen setup
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")
    screen.fill(WHITE)

    drawLines(screen)

    done, running = False, True
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        actions = gameBoard.availablePositions()
        state = gameBoard.getState()

        if first:
            drawBoard(state, screen)
            time.sleep(2) # Wait for 2 seconds to let user process the board
            first = False

        if turn == 1:
            action = agent.chooseAction(state, actions)
            state, done = agent.play(action)
        else:
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit(0)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouseX = event.pos[0]
                        mouseY = event.pos[1]
                    
                        clickedRow: int = mouseY // SQUARESIZE  # mouseX is relative to pygame display window
                        clickedCol: int = mouseX // SQUARESIZE  # mouseY is relative to pygame display window

                        state, done = player.play((clickedRow, clickedCol))

                        waiting = False
        
        drawBoard(state, screen)
        time.sleep(2) # Wait for 2 seconds to let user process the board

        if done:
            if gameBoard.winner is agent:
                drawEndMessage("Computer Won", 60, screen)
            elif gameBoard.winner is player:
                drawEndMessage("Congratulations. You Won!", 30, screen)
            else:
                drawEndMessage("Draw", 60, screen)
        
        turn *= -1
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit(0)

def simulationGame(episodes = 10):
    # Initialize
    pygame.init()
    gameBoard = Board()
    agent = Agent(1, gameBoard)
    bot = Bot(-1, gameBoard)

    # Variables
    turn = random.choice([1, -1])
    first = True

    # Screen setup
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")
    screen.fill(WHITE)

    drawLines(screen)

    done, running = False, True
    for episode in range(episodes):
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

            actions = gameBoard.availablePositions()
            state = gameBoard.getState()

            if first:
                drawBoard(state, screen)
                time.sleep(1) # Wait for 1 second to let user process the board
                first = False

            if turn == 1:
                action = agent.chooseAction(state, actions)
                state, done = agent.play(action)
            else:
                action = bot.chooseAction(state, actions)
                state, done = bot.play(action)

            drawBoard(state, screen)
            time.sleep(1) # Wait for 1 second to let user process the board

            if done:
                if gameBoard.winner is agent:
                    drawEndMessage("Q Learning Agent Won", 30, screen)
                elif gameBoard.winner is bot:
                    drawEndMessage("Minimax Bot Won", 30, screen)
                else:
                    drawEndMessage("Draw", 60, screen)
                
                time.sleep(2) # Sleep 2 seconds for the outcome to be shown
                first, done = restart(screen, gameBoard) 
            
            turn *= -1
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit(0)