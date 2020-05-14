class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        while k > 0:
            if len(num) >= 3:
                case1 = num[0:2] if num[0] != "0" else 99 
                case2 = num[1:3] if num[1] != "0" else 99
                case3 = num[0]+num[2] if num[0] != "0" else 99
                tmp = min([case1, case2, case3])
                num = tmp + num[3:]
            elif len(num) > 1:
                num =  min(''.join(num))
            else:
                num = "0"
            k -= 1
            
        return num

print(Solution().removeKdigits("1231",1))
print(Solution().removeKdigits("1231",2))
print(Solution().removeKdigits("1231",3))
print(Solution().removeKdigits("10",2))