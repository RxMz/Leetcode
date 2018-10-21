class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Runtime: 36 ms, faster than 99.77% of Python3 online submissions for Two Sum.
        temp_1 = {}
        for i in range(len(nums)):
            temp_1[nums[i]] = i
        for i in range(len(nums)):
            if target-nums[i] in temp_1 and temp_1[target-nums[i]] != i:
                return [i, temp_1[target - nums[i]]]
        