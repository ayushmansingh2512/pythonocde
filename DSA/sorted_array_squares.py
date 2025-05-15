#sorted array given an integers array 

class Solution:
    def square_sort(self,nums):

        result = [x * x for x in nums]
        result.sort()
        return result

s = Solution()
a = [-7, -3, 2, 3, 11]
print(s.square_sort(a))
