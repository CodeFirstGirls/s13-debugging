# factorial.py

def factorial(n):
    """Returns the factorial of a number n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def square(n):
    """Returns the square of a number n."""
    return n * n