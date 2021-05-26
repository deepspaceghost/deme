def power(base, exponent):
    """
    This function takes 2 (two) arguments, the first being the base number,
    the second being the exponent. The base number is then raised to the
    power of the expoenent number, and this number is assigned to the
    "power" variable.
    """

    power = base ** exponent
    print(power)


def test_power():
    """
    This function tests the core formula of the power() function.
    """

    base = 2
    exponent = 2
    power = base ** exponent
    assert power == 4.0, "Should be 4.0"


print("Initializing test! (1/1)")
try:
    print("")
    print(power(2, 2))
    test_power()
    print("")
except AssertionError:
    print("Whoops! Execuing an test_power() call got an AssertionError!")
    exit(2)
except AttributeError:
    print("Whoops! Executing a power() call got an AttributeError!")
    exit(2)
except ValueError:
    print("Whoops! Executing a power() call got an ValueError!")
    exit(2)
print("Successful Test! (1/1 COMPLETE)")
print("Terminating!")
exit()
