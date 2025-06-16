def nearest_greater_to_right(arr):

	result = []
	stack = []

	for i in reversed(range(len(arr))):
		while stack and stack[-1] <= arr[i]:
			stack.pop()
		if not stack:
			result.append(-1)
		else:
			result.append(stack[-1])
		stack.append(arr[i])

	return result[::-1]

arr = [1,3,0,0,1,2,4]
print(nearest_greater_to_right(arr))
