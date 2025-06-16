def nearest(arr):
	result = []
	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			if arr[i] < arr[j]:
				result.append(arr[j])
				break
		else:
			
			result.append(-1)
	return result

a = [1,3,2,4]
print(nearest(a))
