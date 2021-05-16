import random


def exercise():
    """
    This function generates a random suggestion for exercise.
    """

    exercises = [
        "Ab workout, 15 minutes",
        "Full body workout, 20 minutes."
    ]

    response = random.choice(exercises)
    print(response)


print("Initializing test! (1/1)")
try:
    print("")
    print(exercise())
    print("")
except AttributeError:
    print("Whoops! Executing a exercise() call got an AttributeError!")
    exit(2)
except ValueError:
    print("Whoops! Executing a exercise() call got an ValueError!")
    exit(2)
print("Successful Test! (1/1 COMPLETE)")
print("Terminating!")
exit()
