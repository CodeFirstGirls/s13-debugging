# test_advanced_operations.py

from advanced_operations import factorial, square, power, sqrt


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


def test_power():
    assert power(3, 2) == 9, "Test failed: power(3,2) should be 9"
    assert power(2, 5) == 32, "Test failed: power(2,5) should be 32"
    assert power(5, 1) == 5, "Test failed: power(5,1) should be 5"
    assert power(4, 0) == 1, "Test failed: power(4,0) should be 1"
    assert power(10, -1) == 0.1, "Test failed: power(10,-1) should be 0.1"


def test_sqrt():
    assert sqrt(1) == 1, "Test failed: sqrt(1) should be 1"
    assert sqrt(4) == 2, "Test failed: sqrt(4) should be 2"
    assert sqrt(225) == 15, "Test failed: sqrt(225) should be 15"
    assert sqrt(0) == 0, "Test failed: sqrt(0) should be 0"
    assert sqrt(15625) == 125, "Test failed: sqrt(15625) should be 125"


if __name__ == "__main__":
    test_factorial()
    test_square()
    test_power()
    test_sqrt()
    print("All tests passed!")
