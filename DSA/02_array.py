# contain duplicates 





try:
    
    a = int(input("Enter the range : "))
    lists = []
    duplicate = set()

    for i in range(a):
        number = int(input(f"Enter the {i+1} number : "))
        lists.append(number)
        duplicate.add(number)



    if len(lists) == len(duplicate):
        print("True No Duplication")
    else:
        print("False there is duplication")


except ValueError:
    # Step 6: If user enters non-numeric input, show error
    print("Please enter valid numbers.")



    
# class Solution(object):
#     def containsDuplicate(self, nums):
#         seen = set()  # this will store unique numbers we've seen so far

#         for num in nums:
#             if num in seen:
#                 return True  # if we've already seen this number, it's a duplicate
#             seen.add(num)  # otherwise, add it to the set

#         return False  # if no duplicates found
