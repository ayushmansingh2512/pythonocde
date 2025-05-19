def singleNumber_HashMap(nums):
    #o(n) ki timing raheingi isme
    first_seen_index = {}
    duplicates = set()

    for idx , num in enumerate(nums):
        if num in first_seen_index:
            duplicates.add(num)
        else:
            first_seen_index[num] = idx


    for num in first_seen_index:
        if num not in duplicates:
            return num




print(singleNumber_HashMap([4, 1, 2, 1, 2]))   # → 4
print(singleNumber_HashMap([2, 2, 3]))         # → 3
print(singleNumber_HashMap([7]))               # → 7

