class Solution(object):
    def guessNumber(self, n):
        low, high = 0, n+1
        while True:
            mid = low +(high-low)//2
            val = guess(mid)
            if val==0:
                return mid
            elif val==1:
                low=mid
            elif val==-1:
                high=mid
        