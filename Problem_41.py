'''
We shall say that an n-digit number is pandigital 
if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
from itertools import permutations
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

digits = "7654321"   # descending so we find the largest first

for p in permutations(digits): # type: ignore
    num = int("".join(p))
    if is_prime(num):
        print(num)
        break
