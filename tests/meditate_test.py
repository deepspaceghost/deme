import time


def meditate():
    """
    """

    meditate = [
        "Bring awareness to your breath.",
        "Breathe in.",
        "Breathe out.",
        "Breathe in.",
        "Breathe out.",
        "Breathe in.",
        "Breathe out.",
        "Breathe in.",
        "Breathe out.",
        "Breathe in.",
        "Breathe out.",
        "Breathe in.",
        "Breathe out."
    ]

    for i in range(13):
        print(meditate[i])
        time.sleep(4.615)


print("Initializing test! (1/1)")
try:
    print("")
    print(meditate())
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
