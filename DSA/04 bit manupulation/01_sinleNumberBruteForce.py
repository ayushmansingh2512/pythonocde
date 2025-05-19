def singleNumber_bruteForce(nums):
    n = len(nums)
    l = []
    for i in range(n):
        found_duplicate = False
        for j in range(n):
            if i!=j and nums[i] == nums[j]:
                found_duplicate = True
                break

        if not found_duplicate:
            return nums[i]
        
print(singleNumber_bruteForce([4, 1, 2, 1, 2]))   # → 4
print(singleNumber_bruteForce([2, 2, 3]))         # → 3
print(singleNumber_bruteForce([7]))               # → 7
           
