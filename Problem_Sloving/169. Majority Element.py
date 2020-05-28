class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        res = Counter(nums).most_common(1)
        return res[0][0]
        