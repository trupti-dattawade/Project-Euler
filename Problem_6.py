"""
The sum of the squares of the first ten natural numbers is,
   1^2+2^2+...+10^2 = 385
The square of the sum of the first ten natural numbers is,
(1+2+...+10)^2 = 55^2 = 3025    
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is   .
3025-385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import math
def sum_square_difference(n: int) -> int:
    """
    Function to calculate the difference between the sum of the squares of the first n natural numbers and the square of the sum.
    :param n: The upper limit for the natural numbers.
    :return: The difference between the sum of the squares and the square of the sum.
    """
    sum_of_squares = sum(i ** 2 for i in range(1, n + 1))
    square_of_sum = sum(range(1, n + 1)) ** 2
    result = square_of_sum - sum_of_squares
    print(result)
    return result

if __name__ == "__main__":
    sum_square_difference(100)
    
#================================
# Solution: 25164150
#================================