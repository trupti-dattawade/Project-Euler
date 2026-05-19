"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from sympy import gcd


def smallest_multiple(n: int) -> int:
    """
    Function to calculate the smallest positive number that is evenly divisible by all of the numbers from 1 to n.
    :param n: The upper limit for the numbers to check divisibility.
    :return: The smallest positive number that is evenly divisible by all of the numbers from 1 to n.
    """
    multiple = 1
    for i in range(2, n + 1):
        multiple *= i // gcd(multiple, i)
    return multiple

if __name__ == "__main__":
    result = smallest_multiple(20)
    print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is:", result)
#================================
# Solution: 232792560
#================================