class Solution:
    def missing_num(self,nums):
            
        nums.sort()
        for i,v in enumerate(nums):
            if i != v:
                return i
        return len(nums)



a = [0,1,2,4]
b = [0,1,2,3]
s = Solution()
print(s.missing_num(a))
print(s.missing_num(b))
