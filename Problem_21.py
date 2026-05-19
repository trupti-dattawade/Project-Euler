'''
Let d(n)  be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
def sum_of_divisors(n: int) -> int:
    """Calculate the sum of proper divisors of n."""
    total = 1  # Start with 1, which is a proper divisor
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:  # Add the complementary divisor if it's different
                total += n // i
    return total

def amicable_numbers(limit: int) -> int:
    """Calculate the sum of all amicable numbers under the given limit."""
    divisor_sums = {}
    for i in range(1, limit):
        divisor_sums[i] = sum_of_divisors(i)

    amicable_sum = 0
    for a in range(1, limit):
        b = divisor_sums[a]
        if b != a and b < limit and divisor_sums.get(b, 0) == a:
            amicable_sum += a

    return amicable_sum
if __name__ == "__main__":
    result = amicable_numbers(10000)
    print(result)