import random
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "major_arcana.txt")) as f:
    trump_cards = [card.rstrip('\r\n ') for card in f.readlines() if card != ""]

with open(os.path.join(dir_path, "minor_arcana_blade_suit.txt")) as f:
    blade_suit_cards = [card.rstrip('\r\n ') for card in f.readlines() if card != ""]

with open(os.path.join(dir_path, "minor_arcana_coin_suit.txt")) as f:
    coin_suit_cards = [card.rstrip('\r\n ') for card in f.readlines() if card != ""]

with open(os.path.join(dir_path, "minor_arcana_cup_suit.txt")) as f:
    cup_suit_cards = [card.rstrip('\r\n ') for card in f.readlines() if card != ""]

with open(os.path.join(dir_path, "minor_arcana_rod_suit.txt")) as f:
    rod_suit_cards = [card.rstrip('\r\n ') for card in f.readlines() if card != ""]

all_cards = trump_cards + blade_suit_cards + coin_suit_cards + cup_suit_cards + rod_suit_cards


def get_card():
    return random.choice(all_cards)
