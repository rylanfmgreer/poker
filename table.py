from player import Player
from deck import Deck
"""
A table. Basically this has a whole bunch of game-state type functions
"""

class Table:
    def __init__(self):
        self.players = []
        self.board = []
        self.deck = Deck()
    
    def add_player(self, player):
        self.players.append(player)

    def rotate_players(self):
        """
        for switching the order, like in dealing.
        """
        self.players = self.players[1:] + [self.players[0]]

    def deal_to_players(self):
        """
        give every player one more card
        """
        for player in self.players: 
            card = self.deck.deal()
            player.recieve_card(card)
    
    def burn(self):
        """
        this shouldn't matter but it's tradition
        """
        self.deck.deal()

    def deal_n_cards(self, n):
        for i in range(n):
            self.board.append(self.deck.deal())

    def flop(self):
        """
        are separate flop, turn, and river functions necessary? not really.
        however, it might aid in readability. Otherwise, no need.
        """
        self.deal_n_cards(3)

    def turn(self):
        self.deal_n_cards(1)

    def river(self):
        self.deal_n_cards(1)

    def copy(self):
        """
        deep copy
        """
        new_table = Table()

        for i in range(len(self.players)):
            pc = self.players[i].copy()
            new_table.add_player(pc)

        new_table.board = self.board.copy()
        new_table.deck = self.deck.copy()

    def calculate_probabilities(self):
        pass


if __name__ == '__main__':
    print('table.py')