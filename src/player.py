class Player:
    def __init__(self, symbol: int, game):
        self.symbol = symbol
        self.game = game
    
    def play(self, position):
        return self.game.step(position, self)
    
    def alternateSymbol(self):
        self.symbol = -1 if self.symbol == 1 else 1