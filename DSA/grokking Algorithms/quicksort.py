# ematy array are easient you can just return them like there was nothing to sort


def quick_sort(arr):
	if len(arr) < 2:
		return arr

	else:
		pivot = arr[0]
		left = [x for x in arr[1:] if x<=pivot]
		right = [x for x in arr[1:] if x > pivot]
		return quick_sort(left) + [pivot] + quick_sort(right)

numbers = [30, 10, 50, 20, 40]
sorted_numbers = quick_sort(numbers)
print(sorted_numbers)