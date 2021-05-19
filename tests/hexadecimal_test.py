def hexadecimal(number: int):
    """
    """

    print("Converting integer...")
    pocus = hex(number)
    print(str(pocus))


def test_hexadecimal():
    """
    """

    number = 9
    assert hex(number) == "0x9", "Should be 0x9"


print("Initializing test! (1/1)")
try:
    print("")
    print(hexadecimal(9))
    test_hexadecimal()
    print("")
except AssertionError:
    print("Whoops! Executing a hexadecimal() call got an AssertionError!")
    exit(2)
except AttributeError:
    print("Whoops! Executing a exercise() call got an AttributeError!")
    exit(2)
except ValueError:
    print("Whoops! Executing a exercise() call got an ValueError!")
    exit(2)
print("Successful Test! (1/1 COMPLETE)")
print("Terminating!")
exit()
