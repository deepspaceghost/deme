import random
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "oblique_strategies.txt")) as f:
    oblique_strategies = [strategy.rstrip('\r\n ') for strategy in f.readlines() if strategy != ""]


def get_strategy():
    return random.choice(oblique_strategies)
