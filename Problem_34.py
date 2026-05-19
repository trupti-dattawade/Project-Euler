'''
145 is a curious number, as  1! + 4! + 5! = 1 + 24 + 120 = 145 .

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''
def factorial(n: int) -> int:
    """Calculate the factorial of n."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result   
def sum_of_factorials(n: int) -> int:
    """Calculate the sum of the factorials of the digits of n."""
    return sum(factorial(int(digit)) for digit in str(n))   
def find_curious_numbers(limit: int) -> list:
    """Find all numbers that are equal to the sum of the factorial of their digits."""
    curious_numbers = []
    for i in range(10, limit):  # Start from 10 since 1! and 2! are not included
        if i == sum_of_factorials(i):
            curious_numbers.append(i)
    return curious_numbers
if __name__ == "__main__":
    # The upper limit is set to 7 * 9! because 9! is the largest factorial of a single digit
    # and a number with more than 7 digits cannot be equal to the sum of the factorials of its digits.
    limit = 7 * factorial(9)
    result = find_curious_numbers(limit)
    print(sum(result))