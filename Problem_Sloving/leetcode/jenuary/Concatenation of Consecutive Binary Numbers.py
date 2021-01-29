class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits,MOD = 0,10 ** 9 + 7
        result = 0
        for i in range(1,n+1):
            if((i & i-1) == 0): digits += 1
            print(i, i-1, (i & i-1), digits, result, (result << digits) + i)
            result = ((result << digits) + i ) % MOD
        return result
    '''
        int digits = 0, MOD = 1000000007;
        long result = 0;
        for(int i = 1; i <= n; i++){
			/* if "i" is a power of 2, then we have one additional digit in
			   its the binary equivalent compared to that of i-1 */
            if((i & (i - 1)) == 0) digits++; 
            result = ((result << digits) + i) % MOD;
        }
        
        return (int) result;
    ''' 


Solution().concatenatedBinary(3)

