class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
 
        if len(nums) < 3: return []
        
        nums = sorted(nums)
        
        for cur in range(1,len(nums)-1):
            p1 = 0
            p2 = len(nums) - 1
            while True:
              if p1 == cur or p2 == cur:
                  break            
              target = nums[p1] + nums[p2] + nums[cur]
              if target == 0:
                  res.add((nums[p1],nums[cur],nums[p2]))
                  p1 = p1 + 1
              elif target > 0:
                  p2 = p2 - 1
              else:
                  p1 = p1 + 1

        return res

Solution().threeSum([-1, 0, 1, 2, -1, -4])