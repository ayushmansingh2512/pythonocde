class Solution:
    def missing_num(self,nums):
        set_num = set(nums)

        rat = []

        for i in range(1,len(nums)+1): # 1,2,3,4,4,5,6,6,7 it will start fom and go to len plus one because len startsf rom zero so we have to increment
            if i not in set_num:
                rat.append(i)



        return rat

a = [4,3,2,7,8,2,3,1]
b=[1,1]

s = Solution()

print(s.missing_num(a))
print(s.missing_num(b))
