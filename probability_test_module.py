# jul 16 2021
import math as m
from evaluation_functions import estimate_probability

N_TRIALS = 100_000

class ProbabilityTest:
    """
    A single probability test.
    Basically just a nice way of formatting the string.
    Might be nice to use if I ever want to do more in testing.
    """
    def __init__(self, public_cards, private_cards, n_players, benchmark, test_name=''):
        self.public_cards = public_cards
        self.private_cards = private_cards
        self.benchmark = benchmark
        self.n_players = n_players
        self.test_name=test_name

    def run_test(self):
        p = estimate_probability(self.private_cards, self.public_cards, self.n_players, N_TRIALS)
        se = m.sqrt(p * (1 - p)/N_TRIALS)
        print_str = """
        Test name: {test}
        Public cards: {public_cards}
        Private Cards: {private_cards}
        Calculated Probability: {prob}
        Benchmark Probability:  {bench}
        Std. Error: {ste}
        """.format(test=self.test_name,
        public_cards=self.public_cards,
        private_cards=self.private_cards,
        prob=p,
        bench=self.benchmark, 
        ste=se)
        print(print_str)

