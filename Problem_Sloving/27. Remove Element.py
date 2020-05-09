class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        res = 0
        for num in nums:
            if num != val:
                res +=1
        
        for i in range(len(nums)-1):
            if nums[i] == val:
                p1 = i
                p2 = i + 1
                while p2 < len(nums):
                    if nums[p2] != val:
                        nums[p1], nums[p2] = nums[p2], nums[p1]
                        p1 = p2
                        p2 = p1 + 1
                    else:
                        p2 += 1

        return res