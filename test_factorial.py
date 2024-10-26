# test_factorial.py

from factorial import factorial

def test_factorial():
    assert factorial(0) == 1, "Test failed: factorial(0) should be 1"
    assert factorial(1) == 1, "Test failed: factorial(1) should be 1"
    assert factorial(5) == 120, "Test failed: factorial(5) should be 120"
    assert factorial(6) == 720, "Test failed: factorial(6) should be 720"

if __name__ == "__main__":
    test_factorial()
    print("All tests passed!")
