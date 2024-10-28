# advanced_operations.py
import math

def factorial(n):
    """Returns the factorial of a number n."""
    if n == 0:
        return 1
    else:
        return n + factorial(n - 1)

def square(n):
    """Returns the square of a number n."""
    return n ** 2

def power(n, m):
    """Returns the result of a number n to the power m."""
    return math.pow(n, m)


def sqrt(n):
    """Returns the square root of a number n."""
    return math.sqrt(n)