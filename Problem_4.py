'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

#================================
def is_palindrome(n: int) -> bool:
    """
    Function to check if a given number n is a palindrome.
    :param n: The number to check for palindrome property.
    :return: True if n is a palindrome, False otherwise.
    """
    s = str(n)
    return s == s[::-1]
def largest_palindrome_product() -> int:
    """
    Function to calculate the largest palindrome made from the product of two 3-digit numbers.
    :return: The largest palindrome product of two 3-digit numbers.
    """
    max_palindrome = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
    return max_palindrome

if __name__ == "__main__":
    result = largest_palindrome_product()
    print("The largest palindrome product of two 3-digit numbers is:", result)
#================================
# Solution: 906609
#================================