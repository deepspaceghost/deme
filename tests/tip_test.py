def tip(meal: float, tip: int, tax: int, people: int):
    """
    This function takes a bill amount and percentage, both floats, and the
    number of people, an integer, and calculates the tip by multiplying the
    bill amount by the percentage. The function then checks the number of
    people, and determines the individual amount basedon this number.
    """

    meal = float(input().strip())
    tip = int(input().strip())
    tax = int(input().strip())
    people = int(input().strip())

    add_tip = meal * (tip / 100)
    add_tax = meal * (tax / 100)
    final_cost = meal + add_tip + add_tax

    if int(people) < 2:
        print(f"Your bill was {meal}.")
        print(f"{tip / 100} of the bill is {add_tip}.")
        print(f"The total is {final_cost}.")

    elif int(people) > 1:
        print(f"The bill was {meal}.")
        print(f"{tip / 100} of the bill is {add_tip}.")
        print(f"Your total is {final_cost / people}.")


def test_tip():
    """
    """

    meal = 23.98
    tip = 20
    tax = 1
    people = 2

    add_tip = meal * (tip / 100)
    add_tax = meal * (tax / 100)

    final_cost = (meal + add_tip + add_tax) / people
    assert final_cost == 14.5079, "Should be 14.5079"


print("Initializing test! (1/1)")
try:
    print("")
    print(tip(23.98, 20, 71, 2))
    test_tip()
    print("")
except AssertionError:
    print("Whoops! Executing a test_tip() call got an AssertionError!")
    exit(2)
except AttributeError:
    print("Whoops! Executing a tip() call got an AttributeError!")
    exit(2)
except ValueError:
    print("Whoops! Executing a tip() call got an ValueError!")
    exit(2)
print("Successful Test! (1/1 COMPLETE)")
print("Terminating!")
exit()
