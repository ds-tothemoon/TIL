class Solution(object):
    def findLHS(self, nums):
        from collections import Counter
        counter = Counter(nums)
        sorted_nums_count = sorted(counter.items())
        res = 0
        for i in range(len(sorted_nums_count)-1):
            if sorted_nums_count[i+1][0] - sorted_nums_count[i][0] == 1:
                res = max(res, sorted_nums_count[i][1] + sorted_nums_count[i+1][1])
        return 
Solution().findLHS([1,3,2,2,5,2,3,7])