def hexadecimal(number: int):
    """
    Handles the command to convert an integer to a
    string object containing two hexadecimal digits.
    """

    print("Converting integer...")
    pocus = hex(number)
    print(str(pocus))


print("Initializing test! (1/1)")
try:
    print("")
    print(hexadecimal(9))
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
