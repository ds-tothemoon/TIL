class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        get_bin = lambda x: format(x, 'b')
        dividend = 10 ** 9 + 7
        tmp = ''
        for i in range(1,n+1):
            tmp += get_bin(i)
        return int(tmp,2) % dividend
Solution().concatenatedBinary(3)

