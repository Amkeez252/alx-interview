#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0


    # Initialize a list to store the minimum number of coins needed for each value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0


    # Update dp array using dynamic programming
    for coin in coins:
        for i in range(coin, total + 1):
            dp[1] = min(dp[1], dp[1 - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
