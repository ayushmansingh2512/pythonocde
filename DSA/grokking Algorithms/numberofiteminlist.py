# Write a recursive function to count the number of items in a list.
def items(nums):
	if not nums:
		return 0
	else:
		return 1 + items(nums[1:])

print(items([10,20,30,40]))



#Find the maximum number in a list.
def maxnumber(nums2):
	if not nums2:
		return 0
	else:
		return max(nums2[0], maxnumber(nums2[1:]))

print(maxnumber([10,20,30,40]))