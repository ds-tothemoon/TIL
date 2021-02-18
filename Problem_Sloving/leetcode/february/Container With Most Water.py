class Solution(object):
    def maxArea(self, height):
        start, end = 0, len(height)-1
        res = 0
        while start < end:
            tmp = (end - start) * min(height[start],height[end])
            res = max(res, tmp)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return res

Solution().maxArea( [1,8,6,2,5,4,8,3,7])