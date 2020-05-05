class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            p1 = i
            if nums[p1] == 0:
                p2 = p1 + 1
                while p1 < len(nums) and p2 < len(nums):
                    if nums[p2] != 0: 
                        nums[p1], nums[p2] = nums[p2], nums[p1]
                        p1 = p2
                        p2 = p1 + 1 
                    else:
                        p2 = p2 + 1

        return nums

print(Solution().moveZeroes([0,1,0,3,12]))
"""
0 1 0 3 12
1 0 0 3 12

"""