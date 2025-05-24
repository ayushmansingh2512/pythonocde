class NumArray(object):
    def __init__(self, nums):
        self.acc_nums=[0]
        for num in nums:
            self.acc_nums.append(self.acc_nums[-1] + num)


        def sunRange(self,left,right):
            return self.acc_nums[righ+1] - self.acc_nums[left]



