class Solution:
    def three_sum(self, nums):
        nums.sort()              # keep output ordered & help skip duplicates
        n = len(nums)
        out = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:   # skip duplicate anchors
                continue

            target = -a
            seen = set()
            j = i + 1

            while j < n:
                b = nums[j]
                c = target - b

                if c in seen:                # found a valid pair (b, c)
                    out.append([a, c, b])    # a ≤ c ≤ b because nums is sorted

                    # skip duplicates of b
                    while j + 1 < n and nums[j + 1] == b:
                        j += 1

                seen.add(b)
                j += 1

        return out
sol = Solution()
print(sol.three_sum([-1, 0, 1, 2, -1, -4]))

