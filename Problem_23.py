'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1+2+4+7+14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1+2+3+4+6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
def sum_of_proper_divisors(n: int) -> int:
    """Calculate the sum of proper divisors of n."""
    total = 1  # Start with 1, which is a proper divisor
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:  # Add the complementary divisor if it's different
                total += n // i
    return total
def abundant_numbers(limit: int) -> list:
    """Generate a list of abundant numbers up to the given limit."""
    return [n for n in range(1, limit) if sum_of_proper_divisors(n) > n]
def abundant_sums(limit: int) -> set:
    """Generate a set of all numbers that can be expressed as the sum of two abundant numbers."""
    abundant_nums = abundant_numbers(limit)
    sums = set()
    for i in range(len(abundant_nums)):
        for j in range(i, len(abundant_nums)):
            s = abundant_nums[i] + abundant_nums[j]
            if s < limit:
                sums.add(s)
            else:
                break
    return sums
def non_abundant_sums(limit: int) -> int:
    """Calculate the sum of all positive integers that cannot be written as the sum of two abundant numbers."""
    abundant_sums_set = abundant_sums(limit)
    return sum(n for n in range(1, limit) if n not in abundant_sums_set)
if __name__ == "__main__":
    result = non_abundant_sums(28124)
    print(result)