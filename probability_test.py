from probability_test_module import ProbabilityTest
import numpy as np

"""
Benchmarking comes from a few sites.
https://www.oddsshark.com/poker
https://pokerfortress.com/7-2-worst-poker-hand/
"""

private_cards = [
    (i, 0) for i in range(14, 9, -1) # straight flush
]
public_cards = []
test = ProbabilityTest(public_cards, private_cards, 1, 1., 'Straight Flush')
test.run_test()

private_cards = [
    (14, 1), (13, 1)
]
public_cards = []
test = ProbabilityTest(public_cards, private_cards, 1, 0.66, 'AK Suited')
test.run_test()

private_cards = [
    (7, 1), (2, 2)
]
public_cards = []
test = ProbabilityTest(public_cards, private_cards, 1, 0.3416, '7-2 offsuit')
test.run_test()

private_cards = [
    (14, 0), (14, 1)
]
public_cards = []

test = ProbabilityTest(public_cards, private_cards, 1, 0.85, 'Pocket Aces')
test.run_test()

private_cards = []
public_cards = []

test = ProbabilityTest(public_cards, private_cards, 1, 0.5, 'No info')
test.run_test()