import random
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "class_a_games.txt")) as f:
    class_a_games = [game.rstrip('\r\n ') for game in f.readlines() if game != ""]

all_games = class_a_games


def get_game():
    """
    """

    return random.choice(all_games)
