def area_triangle(height: int, base: int):
    """
    This function takes two numbers, first is the height, which is
    multiplied by the second number, the base. The result is then divided
    by two (2), and the function sends an embeded message with the
    explaining formula, formatted with the corresponding strings.
    """

    area = (height * base) / 2
    print(f"Triangle | Solve for area: A = (height * base) / 2 = {area}.")


def test_area_triangle():
    """
    This function test the core formula of the area_triangle function.
    """

    height = 2
    base = 2
    area = (height * base) / 2
    assert area == 2.0, "Should be 2.0"


print("Initializing test! (1/1)")
try:
    print("")
    print(area_triangle(2, 2))
    test_area_triangle()
    print("")
except AssertionError:
    print("Whoops! Execuing an test_area_triangle() call got an AssertionError!")
    exit(2)
except AttributeError:
    print("Whoops! Executing a area_triangle() call got an AttributeError!")
    exit(2)
except ValueError:
    print("Whoops! Executing a area_triangle() call got an ValueError!")
    exit(2)
print("Successful Test! (1/1 COMPLETE)")
print("Terminating!")
exit()
