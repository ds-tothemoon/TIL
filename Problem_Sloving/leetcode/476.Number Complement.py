class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        key = 2 **(len(bin(num)) - 2) - 1
        return num ^ key

print(Solution().findComplement(5))