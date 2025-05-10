class Solution:
    def two_num(self,nums):
        temp = sorted(nums)
        d = {}

        
        for i, num in enumerate(temp):
            if num not in d:
                d[num] = i


        ret = []

        for i in nums:
            ret.append(d[i])

        return ret




a = [8,1,2,2,3]

s = Solution()

print(s.two_num(a))


