class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        """
        i=profit=0
        j=1 
        while(j<len(prices)):
            if(prices[j]-prices[i]>0):
                profit += (prices[j]-prices[i])
            i += 1
            j += 1
        return profit
            