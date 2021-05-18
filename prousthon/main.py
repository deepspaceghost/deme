import random
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "proust_questionnaire.txt")) as f:
    proust_questions = [question.rstrip('\r\n ') for question in f.readlines() if question != ""]

with open(os.path.join(dir_path, "inside_the_actor_studio.txt")) as f:
    istudio_questions = [question.rstrip('\r\n ') for question in f.readlines() if question != ""]

with open(os.path.join(dir_path, "vanity_fair.txt")) as f:
    vanity_questions = [question.rstrip('\r\n ') for question in f.readlines() if question != ""]

all_questions = proust_questions + istudio_questions + vanity_questions


def get_question():
    return random.choice(all_questions)
