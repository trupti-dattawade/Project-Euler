'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
def largest_prime_factor(n: int) -> int:
    """
    Function to calculate the largest prime factor of a given number n.
    :param n: The number for which to find the largest prime factor.
    :return: The largest prime factor of n.
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

if __name__ == "__main__":
    result = largest_prime_factor(600851475143)
    print("The largest prime factor of 600851475143 is:", result)
#================================
# Solution: 6857
#================================