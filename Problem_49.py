'''
The arithmetic sequence , 1487,4817,8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the four-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three four-digit primes, exhibiting this property, but there is one other four-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
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


# generate 4-digit primes
primes = [x for x in range(1000, 10000) if is_prime(x)]

# group primes by sorted digits
groups = {}
for p in primes:
    key = ''.join(sorted(str(p)))
    groups.setdefault(key, []).append(p)

for group in groups.values():
    if len(group) < 3:
        continue
    
    group.sort()
    
    for i in range(len(group)):
        for j in range(i+1, len(group)):
            a = group[i]
            b = group[j]
            c = 2*b - a
            
            if c in group and a != 1487:
                print(str(a) + str(b) + str(c))