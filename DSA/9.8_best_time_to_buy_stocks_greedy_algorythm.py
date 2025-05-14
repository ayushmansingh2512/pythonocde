class Solution:
    def maxProfit(self, prices):
        l ,r =  0 , 1
        maxP = 0

        while r!= len(prices):
            if prices[l] < prices[r]:
                prof = prices[r] - prices[l]
                maxP = max(prof, maxP)

            else:
                l=r


            r += 1

        return maxP


s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))

