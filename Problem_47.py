'''
The first two consecutive numbers to have two distinct prime factors are:
14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:
644 = 2^2 × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19
Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''
def prime_factors(n: int) -> set:   
    """Return the set of distinct prime factors of n."""
    factors = set()
    # Check for number of 2s that divide n
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    # n must be odd at this point, so we can skip even numbers
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    # This condition is to check if n is a prime number greater than 2
    if n > 2:
        factors.add(n)
    return factors
def find_consecutive_numbers_with_distinct_prime_factors(count: int) -> int:
    """Find the first of the first 'count' consecutive integers to have 'count' distinct prime factors."""
    consecutive_count = 0
    n = 2  # Start checking from the first prime number
    while True:
        if len(prime_factors(n)) == count:
            consecutive_count += 1
            if consecutive_count == count:
                return n - count + 1  # Return the first of the consecutive numbers
        else:
            consecutive_count = 0
        n += 1
if __name__ == "__main__":
    result = find_consecutive_numbers_with_distinct_prime_factors(4)
    print(result)
    