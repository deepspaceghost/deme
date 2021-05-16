import random


def random_password():
    """
    This function generates a password at random. When a user uses the !rp
    command, followed by the desired length of the password, the function
    pulls from four (4) lists of characters to generate a passowrd matching
    the predeterminded length.
    """

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "123456789"
    symbols = "[]{}()*;/,._-"
    characters = lower + upper + numbers + symbols
    password_length = 24
    password = "".join(random.sample(characters, password_length))
    print(password)


print("Initializing test! (1/1)")
try:
    print("")
    print(random_password())
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
