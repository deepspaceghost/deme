import random


def cleandex(period: str):
    """
    This function pulls an item from a list of cleaning tasks at random.
    The tasks are seperated by suggested frequency, and items can be
    accessed by the user passing either the day, week, or month argument.
    """

    day_tasks = [
        "Have you put clean dishes away today?",
        "Have you swept today?",
        "Have you taken out the trash today?",
        "Have you washed a load of dishes today?",
        "Have you wiped the countertops today?",
        "Have you wiped the kitchen sink out today?"
    ]

    week_tasks = [
        "Have you cleaned the floors this week?",
        "Have you cleaned the mirror(s) this week?",
        "Have you dusted your shelves this week?",
        "Have you vacuumed the apartment / house this week?"
    ]

    month_tasks = [
        "Have you cleaned the vents this month?",
        "Have you organized your dresser drawers this month?",
        "Have you scrubbed the shower grout this month?",
        "Have you vacuumed the car this month?"
    ]

    if period == "day":
        response = random.choice(day_tasks)
        print(response)

    elif period == "week":
        response = random.choice(week_tasks)
        print(response)

    elif period == "month":
        response = random.choice(month_tasks)
        print(response)

    else:
        print("Use 'day', 'week', or 'month' for a more specific task.")


def test_cleandex():
    """
    This function tests the core formula of cleandex().
    """

    day_tasks = [
        "Have you swept today?"
    ]

    period = "day"

    if period == "day":
        response = random.choice(day_tasks)
        assert response == "Have you swept today?", "Should be 'Have you swept today?'"


print("Initializing test! (1/1)")
try:
    print("")
    print(cleandex("day"))
    test_cleandex()
    print("")
except AssertionError:
    print("Whoops! Execuing a call got an AssertionError!")
    exit(2)
except AttributeError:
    print("Whoops! Executing a call got an AttributeError!")
    exit(2)
except ValueError:
    print("Whoops! Executing a call got an ValueError!")
    exit(2)
print("Successful Test! (1/1 COMPLETE)")
print("Terminating!")
exit()
