'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001 st prime number?
'''
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

def nth_prime(n: int) -> int:
    """
    Function to calculate the nth prime number.
    :param n: The position of the prime number to find.
    :return: The nth prime number.
    """
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

if __name__ == "__main__":
    result = nth_prime(10001)
    print("The 10,001st prime number is:", result)

#================================
# Solution: 104743
#================================