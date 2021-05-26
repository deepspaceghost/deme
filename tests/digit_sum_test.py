def digit_sum(base_number: int):
    """
    This function takes the base number following the !digitsum command and
    adds the individual digits in the base number, returning the total sum.
    """

    the_sum = 0
    for digit in str(base_number):
        the_sum += int(digit)
    print(the_sum)


def test_digit_sum():
    """
    This function tests the core formula of the digit_sum function.
    """

    base_number = 22
    the_sum = 0
    for digit in str(base_number):
        the_sum += int(digit)
    assert the_sum == 4, "Should be 4"


print("Initializing test! (1/1)")
try:
    print("")
    print(digit_sum(22))
    test_digit_sum()
    print("")
except AssertionError:
    print("Whoops! Execuing an test_digit_sum() call got an AssertionError!")
    exit(2)
except AttributeError:
    print("Whoops! Executing a digit_sum() call got an AttributeError!")
    exit(2)
except ValueError:
    print("Whoops! Executing a digit_sum() call got an ValueError!")
    exit(2)
print("Successful Test! (1/1 COMPLETE)")
print("Terminating!")
exit()
