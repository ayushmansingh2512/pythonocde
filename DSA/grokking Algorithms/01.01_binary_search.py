def binary_search(nums,target):
    low = 0
    high = len(nums) -1

    while low <= high:
        mid = (low + high) // 2
        guess = nums[mid]

        if guess == target:
            return mid

        elif guess < target:
            low = mid+1
        else:
            high = mid-1
    
    return None

a = [1,3,5,7,9]
        
print(binary_search(a,3))
print(binary_search(a,-1))
