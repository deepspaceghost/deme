def ascii(ascii_code: int):
    """
    Handles the command to convert a ASCII code to an ASCII character.
    """

    chango = chr(ascii_code)
    print(chango)


def test_ascii():
    """
    The function tests the core formula of the ascii() function.
    """

    ascii_code = 100
    chango = chr(ascii_code)
    assert chango == "d", "Should be d"


print("Initializing test! (1/1)")
try:
    print("")
    print(ascii(100))
    test_ascii()
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
