class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        z_shifter = 0
        t_shifter = len(nums) - 1
        passer = 0
        while(passer<=t_shifter):
            if nums[passer] == 1:
                passer+=1
                continue
            if nums[passer] == 0:
                temp = nums[z_shifter]
                nums[z_shifter] = nums[passer]
                nums[passer] = temp
                z_shifter+=1
                passer+=1
            else:
                temp = nums[t_shifter]
                nums[t_shifter] = nums[passer]
                nums[passer] = temp
                t_shifter-=1
