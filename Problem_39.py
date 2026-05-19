'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c} , there are exactly three solutions for p.

120: (20,48,52), (24,45,51), (30,40,50)
For which value of  , is the number of solutions maximised?
'''
def count_solutions(perimeter):
    """Count the number of right angle triangle solutions for a given perimeter."""
    count = 0
    for a in range(1, perimeter):
        for b in range(a, perimeter - a):
            c = perimeter - a - b
            if a**2 + b**2 == c**2:
                count += 1
    return count
if __name__ == "__main__":
    max_solutions = 0
    result_perimeter = 0
    for p in range(1, 1001):
        solutions = count_solutions(p)
        if solutions > max_solutions:
            max_solutions = solutions
            result_perimeter = p
    print(result_perimeter)
    