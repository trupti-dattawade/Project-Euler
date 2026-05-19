'''
Euler discovered the remarkable quadratic formula:

  n^2 + n + 41

It turns out that the formula will produce 40  primes for the consecutive integer values 0<=n<40. However, when n=40,40^2+40+41=40(40+1) is divisible by 41, 
and certainly when n=41,41^2+41+41=41(41+1) is divisible by 41, the formula produces a composite number.

The incredible formula n^2 - 79n + 1601 was discovered, 
which produces 80 primes for the consecutive values 0 ≤ n <= 90. 
The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:
n^2 + an + b, where |a| < 1000 and |b| <= 1000
  , where   and  

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients,  a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''
def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_consecutive_primes(a: int, b: int) -> int:
    """Count the number of consecutive primes produced by the quadratic formula n^2 + an + b."""
    n = 0
    while True:
        value = n**2 + a*n + b
        if not is_prime(value):
            break
        n += 1
    return n
def find_max_prime_producing_quadratic(limit: int) -> int:
    """Find the product of coefficients a and b for the quadratic that produces the maximum number of primes."""
    max_primes = 0
    product_of_coefficients = 0

    for a in range(-limit + 1, limit):
        for b in range(-limit, limit + 1):
            primes_count = count_consecutive_primes(a, b)
            if primes_count > max_primes:
                max_primes = primes_count
                product_of_coefficients = a * b

    return product_of_coefficients
if __name__ == "__main__":
    result = find_max_prime_producing_quadratic(1000)
    print(result)