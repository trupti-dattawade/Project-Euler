'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50=3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''
def is_curious_fraction(numerator: int, denominator: int) -> bool:
    """Check if the fraction numerator/denominator is a curious fraction."""
    num_str = str(numerator)
    den_str = str(denominator)

    # Check for common digits
    for digit in num_str:
        if digit in den_str and digit != '0':
            # Attempt to cancel the common digit
            new_num_str = num_str.replace(digit, '', 1)
            new_den_str = den_str.replace(digit, '', 1)

            if new_num_str and new_den_str:  # Ensure we have digits left after cancellation
                new_numerator = int(new_num_str)
                new_denominator = int(new_den_str)

                # Check if the fractions are equal
                if numerator * new_denominator == denominator * new_numerator:
                    return True

    return False
def find_curious_fractions() -> list:
    """Find all non-trivial curious fractions."""
    curious_fractions = []
    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):  # Ensure the fraction is less than 1
            if is_curious_fraction(numerator, denominator):
                curious_fractions.append((numerator, denominator))
    return curious_fractions
def product_of_fractions(fractions: list) -> (int, int): # type: ignore
    """Calculate the product of the given fractions and return it in lowest terms."""
    from math import gcd

    numerator_product = 1
    denominator_product = 1

    for numerator, denominator in fractions:
        numerator_product *= numerator
        denominator_product *= denominator

    common_divisor = gcd(numerator_product, denominator_product)
    return numerator_product // common_divisor, denominator_product // common_divisor

if __name__ == "__main__":
    curious_fractions = find_curious_fractions()
    numerator, denominator = product_of_fractions(curious_fractions)
    print(denominator)
