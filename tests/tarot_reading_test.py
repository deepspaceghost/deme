import tarot


def test_tarot_reading():
    """
    This function tests the core formula of the tarot_reading() function.
    """

    print("Here is your fortune.")
    print(tarot.get_card())


print("Initializing test! (1/1)")
try:
    print("")
    print(test_tarot_reading())
    print("")
except AttributeError:
    print("Whoops! Executing a call got an AttributeError!")
    exit(2)
except ValueError:
    print("Whoops! Executing a call got an ValueError!")
    exit(2)
print("Successful Test! (1/1 COMPLETE)")
print("Terminating!")
exit()
