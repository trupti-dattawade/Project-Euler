"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
def is_prime(num: int) -> bool:
    """
    Function to check if a given number num is prime.
    :param num: The number to check for primality.
    :return: True if num is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes_below(n: int) -> int:
    """
    Function to calculate the sum of all prime numbers below n.
    :param n: The upper limit (non-inclusive) for calculating the sum of primes.
    :return: The sum of all prime numbers below n.
    """
    total_sum = 0
    for i in range(2, n):
        if is_prime(i):
            total_sum += i
    return total_sum

if __name__ == "__main__":
    result = sum_of_primes_below(2000000)
    print("The sum of all prime numbers below two million is:", result)

#================================
# Solution: 142913828922
#================================