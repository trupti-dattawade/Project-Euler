'''
 n! means n*(n-1)*3*2*1     .

For example,   10!  = 10*9*8*7*6*5*4*3*2*1 = 3628800,
and the sum of the digits in the number  is  3+6+2+8+8+0+0 = 27      .

Find the sum of the digits in the number 100!.
'''
def factorial(n: int) -> int:
    """Calculate the factorial of n."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def sum_of_digits(n: int) -> int:
    """Calculate the sum of the digits of n."""
    return sum(int(digit) for digit in str(n))

if __name__ == "__main__":
    factorial_100 = factorial(100)
    result = sum_of_digits(factorial_100)
    print(result)

# Output: 648