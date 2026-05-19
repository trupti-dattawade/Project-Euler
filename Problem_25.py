'''
The Fibonacci sequence is defined by the recurrence relation:
f(n) = f(n-1) + f(n-2), where f(1) = 1 and f(2) = 1.
  , where   and  .
Hence the first  terms will be:
f(1)=1
f(2)=1  
f(3)=2
f(4)=3
f(5)=5
f(6)=8
f(7)=13
f(8)=21
f(9)=34
f(10)=55
f(11)=89
f(12)=144

The 12th term,f(12), is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''
def fibonacci_with_digits(digits: int) -> int:
    """Return the index of the first Fibonacci term with the specified number of digits."""
    a, b = 1, 1
    index = 2  # Start from the second term

    while True:
        a, b = b, a + b
        index += 1
        if len(str(b)) >= digits:
            return index
if __name__ == "__main__":
    result = fibonacci_with_digits(1000)
    print(result)