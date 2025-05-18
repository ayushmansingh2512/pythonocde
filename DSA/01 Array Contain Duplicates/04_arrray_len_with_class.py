class Solution:
    def duplicate(self,arrays):

        seen = set()

        for num in arrays:
            seen.add(num)


        if len(arrays) == len(seen):
            return True;
        else:
            return False





a = [1,1,2,2,3,4] # output false has duplicate number
b = [1,2,3,4,5,6,7] # output  true has dont have a duplicate number

s = Solution()

print(s.duplicate(a))
print(s.duplicate(b))

