'''
considering all integer combinations of a^b for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5, there are 15 distinct terms:
2^2=4, 2^3=8, 2^4=16, 2^5=32
3^2=9, 3^3=27, 3^4=81, 3^5=243
4^2=16, 4^3=64, 4^4=256
5^2=25, 5^3=125, 5^4=625, 5^5=3125
If we repeat this process for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100, how many distinct terms are in the sequence generated?

'''
values = set()

for a in range(2, 101):
    for b in range(2, 101):
        values.add(a ** b)

print(len(values))