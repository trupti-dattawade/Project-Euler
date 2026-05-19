'''
Take the number 192 and multiply it by each of 1, 2, and 3:

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192 the concatenated product of 192 and (1,2,3).

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2,...,n) where n > 1?
'''
def is_pandigital(num_str: str) -> bool:
    """Check if the number string is 1 to 9 pandigital."""
    return sorted(num_str) == ['1', '2', '3', '4', '5', '6', '7', '8', '9'] 
def concatenated_product(n: int, limit: int) -> str:
    """Generate the concatenated product of n with (1, 2, ..., limit)."""
    return ''.join(str(n * i) for i in range(1, limit + 1)) 
def find_largest_pandigital() -> int:   
    """Find the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product."""
    largest_pandigital = 0
    for n in range(1, 10000):  # n can be at most 4 digits to avoid exceeding 9 digits in concatenation
        for limit in range(2, 10):  # n must be multiplied by at least 2 and at most 9
            pandigital_str = concatenated_product(n, limit)
            if len(pandigital_str) > 9:
                break
            if is_pandigital(pandigital_str):
                largest_pandigital = max(largest_pandigital, int(pandigital_str))
    return largest_pandigital
if __name__ == "__main__":
    result = find_largest_pandigital()
    print(result)