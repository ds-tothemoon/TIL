class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 : return nums[0]
        nums = sorted(nums)
        if nums[0] != nums[1]: return nums[0]
        for i in range(1,len(nums)-1):
            if nums[i-1] != nums[i] and nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]