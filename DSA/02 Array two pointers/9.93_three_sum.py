class Solution:
    def threesum(self,nums,target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+ nums[j] + nums[k] ==  target:
                           return (
                            f"index {i}, value {nums[i]}\n"
                            f"index {j}, value {nums[j]}\n"
                            f"index {k}, value {nums[k]}"
                        )

a = [2, 5,2, 15]
target = 9

s = Solution()
print(s.threesum(a, target))   # -> [2, 0]

