def min_len_subarray(arr, t):
    l = 0
    total = 0
    res = float('inf')

    for r in range(len(arr)):
        total += arr[r]

        while total >= t:
            res = min(res, r - l + 1)
            total -= arr[l]
            l += 1

    return 0 if res == float('inf') else res


a = [2, 3, 1, 2, 4, 3]
print(min_len_subarray(a, 7))   # 2   (subarray [4,3] or [3,4])

