"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example,   3^2 + 4^2 = 9 + 16 = 25 = 5^2   .

There exists exactly one Pythagorean triplet for which  a + b + c = 1000  .
Find the product abc.
"""
def find_pythagorean_triplet(sum_value: int) -> int:
    """
    Function to find the product abc of the Pythagorean triplet for which a + b + c = sum_value.
    :param sum_value: The sum of the triplet (a + b + c).
    :return: The product abc of the triplet.
    """
    for a in range(1, sum_value):
        for b in range(a, sum_value - a):
            c = sum_value - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
    return -1  # Return -1 if no triplet is found

if __name__ == "__main__":
    result = find_pythagorean_triplet(1000)
    print("The product abc of the Pythagorean triplet for which a + b + c = 1000 is:", result)
#================================
# Solution: 31875000
#================================