'''
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953 .

Which prime, below one-million, can be written as the sum of the most consecutive primes?
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
def generate_primes(limit: int) -> list:
    """Generate a list of prime numbers below the given limit."""
    primes = []
    for num in range(2, limit):
        if is_prime(num):
            primes.append(num)
    return primes
def find_longest_consecutive_prime_sum(limit: int) -> int:
    """Find the prime below the limit that can be written as the sum of the most consecutive primes."""
    primes = generate_primes(limit)
    prime_set = set(primes)  # For O(1) lookups
    max_length = 0
    max_prime = 0
    for i in range(len(primes)):
        for j in range(i + max_length, len(primes)):
            prime_sum = sum(primes[i:j])
            if prime_sum >= limit:
                break
            if prime_sum in prime_set:
                current_length = j - i
                if current_length > max_length:
                    max_length = current_length
                    max_prime = prime_sum
    return max_prime
if __name__ == "__main__":
    result = find_longest_consecutive_prime_sum(1000000)
    print(result)