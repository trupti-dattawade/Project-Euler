'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''
def is_pandigital(a: int, b: int, c: int) -> bool:
    """Check if the concatenation of a, b, and c is 1 through 9 pandigital."""
    pandigital_str = str(a) + str(b) + str(c)
    return sorted(pandigital_str) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']
def find_pandigital_products() -> set:
    """Find all products whose multiplicand/multiplier/product identity is 1 through 9 pandigital."""
    products = set()
    for a in range(1, 100):  # Multiplicand can be at most 2 digits
        for b in range(1, 10000):  # Multiplier can be at most 4 digits
            c = a * b
            if is_pandigital(a, b, c):
                products.add(c)
    return products
if __name__ == "__main__":
    pandigital_products = find_pandigital_products()
    result = sum(pandigital_products)
    print(result)