'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
def factorial(n: int) -> int:
    """Calculate the factorial of n."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def nth_lexicographic_permutation(digits: list, n: int) -> str:
    """Calculate the nth lexicographic permutation of the given digits."""
    permutation = []
    k = n - 1  # Convert to zero-based index
    while digits:
        f = factorial(len(digits) - 1)
        index = k // f
        permutation.append(str(digits[index]))
        digits.pop(index)
        k %= f
    return ''.join(permutation)

if __name__ == "__main__":
    digits = list(range(10))
    n = 1000000
    result = nth_lexicographic_permutation(digits, n)
    print(result)