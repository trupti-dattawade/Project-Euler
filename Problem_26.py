'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
1/2  = 0.5
1/3  = 0.(3)
1/4  = 0.25
1/5  = 0.2
1/6  = 0.1(6)
1/7  = 0.(142857)
1/8  = 0.125
1/9  = 0.(1)
1/10 = 0.1

Where 0.1 means 0.100000..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
def recurring_cycle_length(n: int) -> int:
    """Calculate the length of the recurring cycle in 1/n."""
    remainders = {}
    remainder = 1
    position = 0

    while remainder != 0:
        if remainder in remainders:
            return position - remainders[remainder]
        remainders[remainder] = position
        remainder = (remainder * 10) % n
        position += 1

    return 0
def longest_recurring_cycle(limit: int) -> int:
    """Find the value of d < limit for which 1/d has the longest recurring cycle."""
    max_length = 0
    result = 0

    for d in range(1, limit):
        length = recurring_cycle_length(d)
        if length > max_length:
            max_length = length
            result = d

    return result
if __name__ == "__main__":
    result = longest_recurring_cycle(1000)
    print(result)
