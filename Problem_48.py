'''
The series,1^1 + 2^2 + 3^3 + ... + 10^10, is equal to 10405071317... (a very large number with over three thousand digits).

Find the last ten digits of the series,  1^1 + 2^2 + 3^3 + ... + 1000^1000 .
'''
def last_ten_digits_of_series(n: int) -> int:
    """Calculate the last ten digits of the series 1^1 + 2^2 + ... + n^n."""
    total = 0
    for i in range(1, n + 1):
        total += pow(i, i, 10**10)  # Use modular exponentiation to keep only the last ten digits
    return total % 10**10
if __name__ == "__main__":
    result = last_ten_digits_of_series(1000)
    print(result)