'''
The number, 197 , is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 41, 43, and 47.

How many circular primes are there below one million?
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
def rotate_number(n: int) -> list:
    """Generate all rotations of the digits of n."""
    rotations = []
    s = str(n)
    for i in range(len(s)):
        rotations.append(int(s[i:] + s[:i]))
    return rotations
def is_circular_prime(n: int) -> bool:
    """Check if n is a circular prime."""
    for rotation in rotate_number(n):
        if not is_prime(rotation):
            return False
    return True
def count_circular_primes(limit: int) -> int:
    """Count the number of circular primes below the given limit."""
    count = 0
    for i in range(limit):
        if is_circular_prime(i):
            count += 1
    return count
if __name__ == "__main__": 
    result = count_circular_primes(1000000)
    print(result)   