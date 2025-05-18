class Solution:
    def three_sums(self, nums):
        triplets = []
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue  # Skip duplicates for the first element

            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = val + nums[left] + nums[right]

                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    triplets.append([val, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for the second number
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return triplets
sol = Solution()
print(sol.three_sums([-1, 0, 1, 2, -1, -4]))

