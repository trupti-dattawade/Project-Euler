'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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
def is_truncatable_prime(n: int) -> bool:
    """Check if n is a truncatable prime from both left and right."""
    s = str(n)
    # Check right to left truncation
    for i in range(len(s)):
        if not is_prime(int(s[i:])):
            return False
    # Check left to right truncation
    for i in range(len(s)):
        if not is_prime(int(s[:len(s) - i])):
            return False
    return True
def find_truncatable_primes(limit: int) -> list:
    """Find all truncatable primes below the given limit."""
    truncatable_primes = []
    for i in range(10, limit):  # Start from 10 since single-digit primes are not considered
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return truncatable_primes
if __name__ == "__main__":
    # The upper limit is set to 1 million as truncatable primes are relatively rare.
    limit = 1000000
    result = find_truncatable_primes(limit)
    print(sum(result))