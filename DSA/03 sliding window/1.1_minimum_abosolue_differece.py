#minimum Absolute diffrence 
#given an array an disting integer arr finad all the pair of element of elements with with the absolute diffrence of any two elements 
class Solution:
    def minAbsDif(self, arr):
        # 1. sort
        arr.sort()

        # 2. find minimum difference
        min_diff = float('inf')
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i - 1])

        # 3. collect pairs that achieve min_diff
        result = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_diff:
                result.append([arr[i - 1], arr[i]])

        return result


