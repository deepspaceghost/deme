import random
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "shorter_strategies.txt")) as f:
    shorter_strategies = [strategy.rstrip('\r\n ') for strategy in f.readlines() if strategy != ""]

with open(os.path.join(dir_path, "longer_strategies.txt")) as f:
    longer_strategies = [strategy.rstrip('\r\n ') for strategy in f.readlines() if strategy != ""]

all_strategies = shorter_strategies + longer_strategies


def get_strategy():
    return random.choice(all_strategies)
