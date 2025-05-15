class Solution:
    def sortedArraySquare(self, nums):
        # Edge case
        if not nums:
            return nums

        if nums[0] >= 0:
            return [num ** 2 for num in nums]

        # Find index of first non-negative number
        m = 0
        for i, n in enumerate(nums):
            if n >= 0:
                m = i
                break

        A = nums[m:]  # Non-negative numbers
        B = [-n for n in reversed(nums[:m])]  # Reverse negatives and make positive

        def merge(A, B):
            a = b = 0
            ret = []
            while a < len(A) and b < len(B):
                if A[a] < B[b]:
                    ret.append(A[a])
                    a += 1
                else:
                    ret.append(B[b])
                    b += 1

            # Append remaining elements
            if a < len(A):
                ret.extend(A[a:])
            else:
                ret.extend(B[b:])
            return ret

        merged = merge(A, B)
        return [n ** 2 for n in merged]


s = Solution()
a = [-4, -1, 0, 3, 10]
print(s.sortedArraySquare(a))  # Output: [4, 9, 9, 49, 121]

