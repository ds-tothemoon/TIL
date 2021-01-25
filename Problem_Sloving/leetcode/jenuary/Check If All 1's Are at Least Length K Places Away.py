class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        answer = []
        tmp = 0
        start = False
        for num in nums:
            if num == 0:
                if start:
                    tmp += 1
            else:
                if start:
                    answer.append(tmp)
                    tmp = 0
                else:
                    start = True
        if answer:
            return min(answer) == k
        else:
            return True