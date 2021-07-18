# jul 16 2021
"""
This is a script for playing a live game and trying to estimate your probability of winning.
"""
from evaluation_functions import estimate_probability

private_cards = []
public_cards = []

intro_str = """
Hand beginning.

To input cards: input the number (if a number card),
11 if Jack, 12 if Queen, 13 if King, 14 if Ace.

Suit choice is arbitrary, but to keep it straight,
you can use 0 for Spades, 1 for Clubs,
2 for Diamonds, 3 for Hearts.
"""
num_str  = "Enter card number: "
suit_str = "Enter card suit:   "


