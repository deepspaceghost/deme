import math


def side_square(number: int):
    side = math.sqrt(number)
    print(f"Square | Solve for side: a = square root of an area = {side}")


print("Initializing test! (1/1)")
try:
    print("")
    print(side_square(25))
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
