from player import Player
from table import Table

class Game:
    def __init__(self, n_players):
        self.table = Table()

        for i in range(n_players):
            pl = Player()
            self.table.add_player(pl)
        
        self.round = 0 # pre-betting, flop, turn, river...

    def advance(self):
        """
        go to the next "round" or stage in the game.
        """
        round = self.round
        if round == 0: # Two cards have not yet been dealt. Advance deals two cards
            for i in range(2):
                self.table.deal_to_players()

        elif round == 1:
            self.table.flop()

        elif round == 2:
            self.table.turn()

        elif round == 3:
            self.table.river()

        round += 1

    def copy(self):
        new_game = Game()
        new_game.table = self.table.copy()
        new_game.round = self.round
        return new_game

