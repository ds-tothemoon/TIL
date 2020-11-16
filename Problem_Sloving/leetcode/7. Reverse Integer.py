class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        answer = 0
        if x < 0:
            answer = -int(str(-x)[::-1])
        else:
            answer =  int(str(x)[::-1])
    
        if answer < -2**31 or answer > (2**31) - 1:
            return 0
        else:
            return answer