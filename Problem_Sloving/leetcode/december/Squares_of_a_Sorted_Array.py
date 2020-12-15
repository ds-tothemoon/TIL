class Solution(object):
    def sortedSquares(self, nums):
        return list(sorted(map(lambda x: x ** 2, nums)))
        
Solution().sortedSquares([-4,-1,0,2,4,100])