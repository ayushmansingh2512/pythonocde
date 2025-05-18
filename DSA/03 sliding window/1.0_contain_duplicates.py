# given integer array and an integer k return true if thre two disting indexs
class Solution:
    def contain_duplicate(self,nums,k):
        seen = set()

        for i , num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            
            if len(seen) > k:
                seen.remove(nums[i-k])

        return False



s = Solution()
a = [1, 2, 3,4, 1]
print(s.contain_duplicate(a, 3))  # True
