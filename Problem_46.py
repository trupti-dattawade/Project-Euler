'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''
def is_prime(n: int) -> bool:
    """Check if n is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def can_be_written_as_sum(n: int) -> bool:
    """Check if n can be written as the sum of a prime and twice a square."""
    for i in range(1, int(n**0.5) + 1):
        square = 2 * (i ** 2)
        if square >= n:
            break
        if is_prime(n - square):
            return True
    return False
def find_smallest_odd_composite() -> int:
    """Find the smallest odd composite that cannot be written as the sum of a prime and twice a square."""
    n = 9  # Start with the first odd composite number
    while True:
        if not is_prime(n) and not can_be_written_as_sum(n):
            return n
        n += 2  # Check only odd numbers
if __name__ == "__main__":    
    result = find_smallest_odd_composite()
    print(result)   