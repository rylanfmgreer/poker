## jul 11 2021
from evaluation_functions import get_all_hands, compare_hands, estimate_probability
N_TRIALS = 100_000 # for monte carlo stuff.

class Player:
    """
    A generic poker player class.
    Most of the functions are fairly self explanatory.
    """

    def __init__(self):
        self.cards_private = []
        self.cards_public = None
        self.table = None
        self.folded = False
        self.expected_value = 0

    def recieve_card(self, card):
        self.cards.append(card)

    def add_to_table(self, table):
        self.table = table
        
    def copy(self):
        """
        Copying is important if I want to do monte carlo simulations at a table level.
        """
        new_player = Player()
        new_player.cards_private = self.cards_private.copy()
        new_player.expected_value = self.expected_value
        return new_player

    def get_all_hands(self):
        return get_all_hands(self.cards_private + self.cards_public)

    def fold(self):
        self.folded = True

    def estimate_probability(self):
        """
        Estimate probability of winning.
        """
        assert self.table is not None # no point of calculating if you're not at a table.
        n_others = len(self.table.players) - 1
        public_cards = self.table.board
        return estimate_probability(self.cards, public_cards, n_others, N_TRIALS)


if __name__ == '__main__':
    print('player')