def nearest_greater_to_left(arr):
	result = []
	stack = []

	for i in range(len(arr)):
		while len(stack) > 0 and stack[-1] <= arr[i]:
			stack.pop()

		if len(stack) == 0:
			result.append(-1)
		else:
			result.append(stack[-1])

		stack.append(arr[i])
	return result

arr = [1,3,2,4]

print(nearest_greater_to_left(arr))