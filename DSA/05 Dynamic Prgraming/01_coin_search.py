def coinChange(coins,amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1 , amount+1):
        for c in coins:
            if (i-c) >= 0:
                dp[i] = min(dp[i],1+ dp[i -c])

    return dp[amount] if (dp[amount] != amount+1) else -1
print(coinChange([1, 2, 5], 11))  # Output: 3 (5 + 5 + 1)
print(coinChange([2], 3))        # Output: -1 (Not possible)



