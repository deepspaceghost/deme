import random
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "food_and_cooking.txt")) as f:
    food_and_cooking_errors = [error.rstrip('\r\n ') for error in f.readlines() if error != ""]

all_errors = food_and_cooking_errors


def get_error():
    return random.choice(all_errors)
