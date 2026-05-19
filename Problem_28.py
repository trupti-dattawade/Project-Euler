'''
Starting with the number  and moving to the right in a clockwise direction a  by  spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is .

What is the sum of the numbers on the diagonals in a  by  spiral formed in the same way?
'''
n = 1001
layers = (n - 1) // 2

total = 1  # center

for k in range(1, layers + 1):
    total += 16*k*k + 4*k + 4

print(total)