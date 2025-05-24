def max_subarray(nums):
    ret = nums[0]
    cs = nums[0]
    
    for i in range(1,len(nums)):
        cs = max(nums[i], cs + nums[i])
        ret = max(ret,cs)

    return ret

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))  # Output: 6


