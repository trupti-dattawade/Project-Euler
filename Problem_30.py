'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1=1^4  is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
def sum_of_fifth_powers(n: int) -> int:
    """Calculate the sum of the fifth powers of the digits of n."""
    return sum(int(digit) ** 5 for digit in str(n)) 
def find_numbers(limit: int) -> list:
    """Find all numbers that can be written as the sum of fifth powers of their digits."""
    numbers = []
    for i in range(2, limit):
        if i == sum_of_fifth_powers(i):
            numbers.append(i)
    return numbers
if __name__ == "__main__":
    # The upper limit is set to 6 * 9^5 because 9^5 is the largest fifth power of a single digit
    # and a number with more than 6 digits cannot be equal to the sum of the fifth powers of its digits.
    limit = 6 * (9 ** 5)
    result = find_numbers(limit)
    print(sum(result))