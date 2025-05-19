class Solution:
    def singleNumber(self,nums):
        xor = 0
        for n in nums:
            xor ^= n 
        return xor

print(Solution().singleNumber([4, 1, 2, 1, 2]))  # 4
print(Solution().singleNumber([2, 2, 3]))        # 3
print(Solution().singleNumber([7]))              # 7

