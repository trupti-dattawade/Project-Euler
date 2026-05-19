'''
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''
def count_ways(total, coins):
    """Count the number of ways to make the total using the given coins."""
    ways = [0] * (total + 1)
    ways[0] = 1  # There is one way to make the total of 0: use no coins

    for coin in coins:
        for i in range(coin, total + 1):
            ways[i] += ways[i - coin]

    return ways[total]  
if __name__ == "__main__":
    total = 200  # Total in pence
    coins = [1, 2, 5, 10, 20, 50, 100, 200]  # Coin denominations in pence
    result = count_ways(total, coins)
    print(result)