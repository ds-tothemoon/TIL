class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s_list = s.split()
        if s_list == []:
            return 0
        return len(s_list[-1])