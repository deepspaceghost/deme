def fahrenheit_from(celsius: int):
    """
    This function takes the celsius, multiplies, divides, and adds to
    convert it to fahrenheit, rounds the number to digits, and sends the
    final number as a string.
    """

    fahrenheit = float(celsius) * 9 / 5 + 32
    fahrenheit = round(fahrenheit, 3)
    print(str(fahrenheit))


def test_fahrenheit_from():
    """
    This function test the core formula of the fahrenheit_from function.
    """

    celsius = float(-15.6 * 9 / 5 + 32)
    fahrenheit = round(celsius, 3)
    assert fahrenheit == 3.92, "should be 3.92"


print("Initializing test! (1/1)")
try:
    print("")
    print(fahrenheit_from(-15.6))
    test_fahrenheit_from()
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
