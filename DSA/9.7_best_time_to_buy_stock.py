class Solution:
    def max_profit(self,prices):
        max_profit = 0
        n = len(prices)

        for i in range(n):
            for j in range(i+1,n):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit,profit)
        return max_profit

prices = [7,1,5,3,6,4]
s = Solution()

print(s.max_profit(prices))
            

