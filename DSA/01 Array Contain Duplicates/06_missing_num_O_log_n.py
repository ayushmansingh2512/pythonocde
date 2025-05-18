class Solution:
    def missing_number(self,nums):

        return sum(range(len(nums)+1)) - sum(nums)



a = [0,1,3]

b = [0,1,3]

s = Solution()

print(s.missing_number(a))
print(s.missing_number(b))
