from board import Board

class Player:
    def __init__(self, symbol: int, game: Board):
        self.symbol = symbol
        self.game = game
    
    def play(self, position):
        return self.game.step(position, self)