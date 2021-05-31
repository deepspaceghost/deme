import random
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "food_and_cooking.txt")) as f:
    food_and_cooking_errors = [error.rstrip('\r\n ') for error in f.readlines() if error != ""]

with open(os.path.join(dir_path, "law_crime_and_military.txt")) as f:
    law_crime_and_military_errors = \
        [error.rstrip('\r\n ') for error in f.readlines() if error != ""]

with open(os.path.join(dir_path, "music.txt")) as f:
    music_errors = [error.rstrip('\r\n ') for error in f.readlines() if error != ""]

with open(os.path.join(dir_path, "religion.txt")) as f:
    religion_errors = [error.rstrip('\r\n ') for error in f.readlines() if error != ""]

with open(os.path.join(dir_path, "sports.txt")) as f:
    sports_errors = [error.rstrip('\r\n ') for error in f.readlines() if error != ""]

all_errors = food_and_cooking_errors + \
    law_crime_and_military_errors + music_errors + religion_errors + sports_errors


def get_error():
    return random.choice(all_errors)
