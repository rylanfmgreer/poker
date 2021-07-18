# jul 18 2021
class Hand:
    """
    A poker hand. Useful for determining what hands a person has.
    """
    def __init__(self, cards):
        self.cards = cards
    
    def get_cards(self):
        """
        Return all cards.
        """
        return self.cards

    def get_nums(self):
        """
        Return only the numerical value of the cards.
        """
        return [card[0] for card in self.cards]
    
    def get_suits(self):
        """
        Return only the suit of the cards.
        """
        return [card[1] for card in self.cards]