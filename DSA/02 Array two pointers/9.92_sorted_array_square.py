import collections
class Solution:
    def sort_array(self,nums):
        answer = collections.deque()
        
        l,r = 0, len(nums) -1
        while l <= r:
            left, right = abs(nums[l]) , abs(nums[r])
            if left > right:
                answer.appendleft(left*left)
                l += 1
            else:
                answer.appendleft(right * right)
                r -= 1

        return list(answer)

s = Solution()
result = s.sort_array([-4, -1, 0, 3, 10])
print(result)  # Output: [0, 1, 9, 16, 100]

