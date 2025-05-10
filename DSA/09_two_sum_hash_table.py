class Solution:
    def two_sum(self,nums,target):
        hashMap = {}
        

        for index , value in enumerate(nums):
            diff = target - value

            if diff in hashMap:
                return [index ,hashMap[diff]]
            
            hashMap[value] = index


a = [2,11,7,15]

s = Solution()

print(s.two_sum(a,9))

