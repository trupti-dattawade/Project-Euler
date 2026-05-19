"""
The following iterative sequence is defined for the set of positive integers:

  n->n/2 (if n is even)
  n->3n+1 (if n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13->40->20->10->5->16->8->4->2->1
It can be seen that this sequence (starting at 13  and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
def collatz_length(n, cache):
    """Return the length of the Collatz chain for n using memoization."""
    original_n = n
    length = 0

    while n != 1 and n not in cache:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1

    # Add known cached length if available
    length += cache.get(n, 1)

    cache[original_n] = length
    return length


limit = 1_000_000
cache = {1: 1}

max_length = 0
starting_number = 0

for i in range(1, limit):
    length = collatz_length(i, cache)
    if length > max_length:
        max_length = length
        starting_number = i

print("Starting number:", starting_number)

# Output:837799