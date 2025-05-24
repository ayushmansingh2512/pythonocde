class Solution:
    def binary_search(self , nums ,t):
        nums.sort()
        l,r = 0 , len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == t:
                return m
            elif nums[m] < t:
                l= m+1
            else:
                r=m-1
        return -1


s = Solution()
a = [1,2,10,32,54,87,92,100]
print(s.binary_search(a,92))
