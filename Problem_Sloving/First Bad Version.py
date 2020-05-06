# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        old = 1
        new = n
        mid = (new + old) // 2
        
        while old < new:
            if new - old == 1:
                if isBadVersion(old):
                    mid = old
                    break
                else:
                    mid = new
                    break
            # exist first bad one before mid
            if isBadVersion(mid):
                new = mid
                mid = (old + new) // 2
            else:
                old = mid
                mid = (old + new) // 2
        if isBadVersion(old):
            return old
        else:
            return mid