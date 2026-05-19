'''
The decimal number, 585 (binary 1001001001), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 2 and base 10.
(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
def is_palindrome(n: int) -> bool:
    """Check if n is a palindrome in base 10."""
    s = str(n)
    return s == s[::-1]
def is_binary_palindrome(n: int) -> bool:
    """Check if n is a palindrome in base 2."""
    b = bin(n)[2:]  # Convert to binary and remove the '0b' prefix
    return b == b[::-1]
def find_double_base_palindromes(limit: int) -> list:
    """Find all numbers less than limit that are palindromic in both base 10 and base 2."""
    double_base_palindromes = []
    for i in range(limit):
        if is_palindrome(i) and is_binary_palindrome(i):
            double_base_palindromes.append(i)
    return double_base_palindromes
if __name__ == "__main__":
    result = find_double_base_palindromes(1000000)
    print(sum(result))