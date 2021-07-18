# jul 11, 2021
import random
from helper_functions import *
from deck import Deck
"""
The general interface:
input: list of cards (five cards)
output: a score basd on the hand in question, where a higher score wins.
        This depends heavily on the hand. As an example, the score for a pair is
        1000 * (pair value) + high card.

        Scores from different types of hands cannot be compared.

        If there is no such hand, return -1.

"""

hands = [
    'straight flush',
    'four of a kind', 
    'full house',
    'flush',
    'straight',
    'three of a kind',
    'two pair',
    'pair',
    'high card'
]

def high_card(l):
    """
    Return the highest single value card.
    """
    vals = [obj[0] for obj in l]
    vals.sort()
    return vals[-1]

def pair(l):
    """
    Return a pair score. The pair score is given as:
    1000 * (highest value pair) + (high card)
    """
    d = number_dict(l)
    pair_list = []
    highest_unpaired_card = highest_unpaired(d)

    for obj in l:
        val, suit = obj
        if d[val] == 2:
            pair_list.append(val)
        if d[val] == 1 and val > highest_unpaired_card:
            highest_unpaired_card = val

    if len(pair_list) > 0:
        pair_list.sort()
        return pair_list[-1] * 1000 + highest_unpaired_card
    
    return -1

def two_pair(l):
    """
    Return a two-pair score. The twopair score is given by:
    1_000_000 * highest pair + 1_000 * second highest pair + high card
    """
    d = number_dict(l)
    highest_unpaired_card = highest_unpaired(d)
    pair_list = []

    for obj in l:
        val, suit = obj
        if d[val] == 2:
            pair_list.append(val)

    if len(pair_list) > 1:
        pair_list.sort()
        return 1_000_000 * pair_list[-1] + 1_000 * pair_list[-2] + highest_unpaired_card

    return -1

def three_of_a_kind(l):
    """
    Return a 3OAK score.
    1000 * (value of card with 3) + high card
    """
    d = number_dict(l)
    highest_unpaired_card = highest_unpaired(d)
    toak_list = []
    for obj in d.keys():
        val = obj
        if d[val] == 3:
            toak_list.append(val)
    if len(toak_list) > 0:
        toak_list.sort()
        return 1000 * toak_list[-1] + highest_unpaired_card

    return -1

def four_of_a_kind(l):
    """
    Return the highest value four of a kind. (Only one can exist in a hand of seven possible cards.)
    """
    d = number_dict(l)
    highest_unpaired_card = highest_unpaired(d)
    for obj in d.keys():
        if d[obj] == 4:
            return 1000 * obj + highest_unpaired_card

    return -1

def full_house(l):
    """
    If a full house exists, return full house score.
    Full house score: 1000 * (card with 3) + (card with two)
    Return False otherwise.
    """
    two = pair(l)
    three = three_of_a_kind(l)
    if two and three:
        return 1000 * three + two

    return -1

def flush(l):
    """
    Return the value of the highest card in the flush if a flush exists (five of the same suit)
    Return False otherwise.
    """
    d = suit_dict(l)
    k = list(d.keys())
    flush_exists = False
    for key in k:
        if d[key] == 5:
            flush_exists = True
            flush_suit = key

    if flush_exists:
        suited_nums = []
        for card in l:
            if card[1] == flush_suit:
                suited_nums.append(card[0])
        return max(suited_nums)

    else:
        return -1

def straight(l):
    """
    Return the highest number in the straight, if a straight exists.
    Return False otherwise.
    """
    nums = [obj[0] for obj in l]
    nums = set(nums)

    # start with 10 J Q K A, end with 2 3 4 5 6.
    # The worst straight will be a special case at the end.
    for i in range(10, 1, -1):
        s = {i, i + 1, i + 2, i + 3, i + 4}
        if s.issubset(nums):
            return i + 4

    # Check to see if A 2 3 4 5 in there, return 5 (the highest value) if so.
    s = {14, 2, 3, 4, 5}
    if s.issubset(nums):
        return 5

    return -1
    
def straight_flush(l):
    """
    Having a straight and a flush dos not guarantee that there is a straight flush.
    This function will check for a flush. If it exists, it will filter out all cards that are not of that suit
    and check for a straight.
    """
    d = suit_dict(l)
    flush_exists = False

    # Can't just use the flush function as we need the suit also.
    for key in d.keys():
        if d[key] > 4:
            flush_exists = True
            flush_suit = key
    
    if flush_exists is False:
        return -1

    # Filter out the cards that aren't in the suit
    suited_cards = []
    for obj in l:
        if obj[1] == flush_suit:
            suited_cards.append(obj)
    
    return straight(suited_cards)

def get_all_hands(l):
    d = {
        'high card': high_card(l),
        'pair': pair(l),
        'two pair': two_pair(l),
        'three of a kind': three_of_a_kind(l),
        'straight': straight(l),
        'flush': flush(l),
        'full house': full_house(l),
        'four of a kind': four_of_a_kind(l),
        'straight flush': straight_flush(l)
    }
    return d

def compare(list_of_dicts, hand_type):

    # Get the list of outcomes.
    outcomes = []
    for d in list_of_dicts:
        v = d[hand_type]
        outcomes.append(v)
    
    # Return false if there are no "hits".
    if all_x(outcomes, -1):
        return -1

    mxs = argmax(outcomes)
    if len(mxs) == 1:
        return mxs[0]
    else:
        random.shuffle(mxs)
        return mxs[0]     

def compare_hands(list_of_dicts):
    for hand in hands:
        b = compare(list_of_dicts, hand)
        if b > -1:
            return b

def one_simulation(private_cards, public_cards, n_players):
    """
    Simulate one hand of poker given the parameters
    """
    # fresh deck of cards
    deck = Deck()

    # all known cards -- remove them from the deck
    cards = private_cards + public_cards
    for card in cards:
        deck.deal_specific_card(card)

    # If I don't have enough cards?
    n_private = 2 - len(private_cards)
    for i in range(n_private):
        private_cards = private_cards + [deck.deal()]

    # deal the rest of the public cards
    n = 5 - len(public_cards)
    for i in range(n):
        public_cards = public_cards + [deck.deal()]
    my_hand = private_cards + public_cards
    assert len(my_hand) == 7

    # deal two cards for every other player.
    other_hands = []
    for i in range(n_players):
        other_hand = []
        for j in range(2):
            other_hand = other_hand + [deck.deal()]
        assert len(other_hand) == 7
        other_hands.append(other_hand + public_cards)
    
    # find the winner
    all_hands = [my_hand] + other_hands
    dicts = [get_all_hands(hand) for hand in all_hands]
    winner = compare_hands(dicts)
    if winner == 0:
        return 1
    return 0

def estimate_probability(private_cards, public_cards, n_players, n_trials):
    c = 0
    for i in range(n_trials):
        c += one_simulation(private_cards, public_cards, n_players)
    p = c/n_trials
    return p


if __name__ == '__main__':
    l = [
        (14, 1),
        (13, 1),
        (12, 1),
        (11, 1),
        (10, 1)
    ]
    print(l)
    print(straight_flush(l))
    print(pair(l))