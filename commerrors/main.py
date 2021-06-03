import random
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "ancient.txt")) as f:
    ancient_errors = [error.rstrip('\r\n ') for error in f.readlines() if error != ""]

with open(os.path.join(dir_path, "architecture.txt")) as f:
    architecture_errors = [error.rstrip('\r\n ') for error in f.readlines() if error != ""]

with open(os.path.join(dir_path, "early_modern.txt")) as f:
    early_modern_errors = [error.rstrip('\r\n ') for error in f.readlines() if error != ""]

with open(os.path.join(dir_path, "film_and_television.txt")) as f:
    film_and_television_errors = [error.rstrip('\r\n ') for error in f.readlines() if error != ""]

with open(os.path.join(dir_path, "food_and_cooking.txt")) as f:
    food_and_cooking_errors = [error.rstrip('\r\n ') for error in f.readlines() if error != ""]

with open(os.path.join(dir_path, "language.txt")) as f:
    language_errors = [error.rstrip('\r\n ') for error in f.readlines() if error != ""]

with open(os.path.join(dir_path, "law_crime_and_military.txt")) as f:
    law_crime_and_military_errors \
        = [error.rstrip('\r\n ') for error in f.readlines() if error != ""]

with open(os.path.join(dir_path, "middle_ages_and_renaissance.txt")) as f:
    middle_ages_and_renaissance_errors \
        = [error.rstrip('\r\n ') for error in f.readlines() if error != ""]

with open(os.path.join(dir_path, "modern.txt")) as f:
    modern_errors = [error.rstrip('\r\n ') for error in f.readlines() if error != ""]

with open(os.path.join(dir_path, "music.txt")) as f:
    music_errors = [error.rstrip('\r\n ') for error in f.readlines() if error != ""]

with open(os.path.join(dir_path, "religion.txt")) as f:
    religion_errors = [error.rstrip('\r\n ') for error in f.readlines() if error != ""]

with open(os.path.join(dir_path, "sports.txt")) as f:
    sports_errors = [error.rstrip('\r\n ') for error in f.readlines() if error != ""]

all_errors = ancient_errors + architecture_errors + early_modern_errors \
    + film_and_television_errors + food_and_cooking_errors + language_errors \
    + law_crime_and_military_errors + middle_ages_and_renaissance_errors + modern_errors \
    + music_errors + religion_errors + sports_errors


def get_error():
    return random.choice(all_errors)
