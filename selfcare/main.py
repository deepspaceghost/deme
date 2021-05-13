import random
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "open_your_notebook.txt")) as f:
    journal_practices = [care.rstrip('\r\n ') for care in f.readlines() if care != ""]

with open(os.path.join(dir_path, "put_your_phone_down.txt")) as f:
    unplugged_practices = [care.rstrip('\r\n ') for care in f.readlines() if care != ""]

with open(os.path.join(dir_path, "take_care_of_yourself.txt")) as f:
    personal_practices = [care.rstrip('\r\n ') for care in f.readlines() if care != ""]

all_practices = journal_practices + unplugged_practices + personal_practices


def get_care():
    return random.choice(all_practices)
