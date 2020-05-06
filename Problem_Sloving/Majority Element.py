class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        counter = Counter(nums)
        majority = len(nums) // 2
        for key in counter:
            if counter[key] > majority:
                return key