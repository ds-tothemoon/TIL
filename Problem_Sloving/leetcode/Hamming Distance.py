class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        cnt = 0
        for i in range(32):
            cnt += (xor >> i) & 1
        return cnt