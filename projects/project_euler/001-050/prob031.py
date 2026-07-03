coins = [1, 2, 5, 10, 20, 50, 100, 200]

def num_ways(n, coins):
    """Determines the number of ways that n can be written as a sum of coins.

    Uses an inefficient top-down approach.
    """
    if n == 0:
        return 1
    return sum(num_ways(n - c, coins[:i + 1]) for i, c in enumerate(coins) if n - c >= 0)

print(num_ways(200, coins))
