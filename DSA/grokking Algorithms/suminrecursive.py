#sun with loops

# def sum(arr):
#     total = 0
#     for i in arr:
#         total += i
#     return total
# print(sum([2,4,6]))


# here the same oprogram with recusrsion

def custom_sum(arr):
    if not arr:
        return 0
    else:
        return arr[0] + custom_sum(arr[1:])

print(sum([2,4,6]))
    