def nearest_greater_to_left(arr):
	result = []
	for i in range(len(arr)):
		for j in range(i - 1 ,-1,-1):
			if arr[j] > arr[i]:
				result.append(arr[j])
				break
		else:
			result.append(-1)
	return result


arr = [1,3,2,4]
print(nearest_greater_to_left(arr))
