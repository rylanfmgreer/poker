# jul 11, 2021
import numpy as np
import random

class Deck:
    """
    Deck of cards with simple functions.
    Pre-shuffled!
    """
    def __init__(self):
        
        vals = np.arange(2, 15) # ace is 14
        suits = np.arange(4)
        cards = []

        for val in vals:
            for suit in suits:
                card = (val, suit)
                cards.append(card)
        random.shuffle(cards)

        self.cards_unused = cards
        self.cards_used = []

    def copy(self):
        """
        Copy. Used in the simulation process, primarily.
        """
        new_deck = Deck()
        new_deck.cards_unused = self.cards_unused.copy()
        new_deck.cards_used = self.cards_used.copy()

    def deal(self):
        """
        Deal one card
        """
        card = self.cards_unused.pop()
        self.cards_used.append(card)
        return card

    def deal_specific_card(self, card_to_deal):
        """
        used to set up a specific game state.
        the use is a little strange but it's meant to work nicely without special cases.
        """
        assert card_to_deal not in self.cards_used
        self.cards_unused.remove(card_to_deal)
        self.cards_used.append(card_to_deal)
        return card_to_deal


if __name__ == '__main__':
    d = Deck()
    print('start:', d.cards_unused)
    print('deal three')
    for i in range(3):
        print(d.deal())
    print('unused:', d.cards_unused)
    print('used:', d.cards_used)


        

