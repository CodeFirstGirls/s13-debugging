# test_advanced_operations.py

from advanced_operations import factorial, square


def test_factorial():
    assert factorial(0) == 1, "Test failed: factorial(0) should be 1"
    assert factorial(1) == 1, "Test failed: factorial(1) should be 1"
    assert factorial(5) == 120, "Test failed: factorial(5) should be 120"
    assert factorial(6) == 720, "Test failed: factorial(6) should be 720"
    assert factorial(7) == 5040, "Test failed: factorial(7) should be 5040"


def test_square():
    assert square(2) == 4, "Test failed: square(2) should be 4"
    assert square(3) == 9, "Test failed: square(3) should be 9"
    assert square(4) == 16, "Test failed: square(4) should be 16"
    assert square(5) == 25, "Test failed: square(5) should be 25"
    assert square(6) == 36, "Test failed: square(6) should be 36"


if __name__ == "__main__":
    test_factorial()
    test_factorial()
    print("All tests passed!")
