class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        k = len(t)
        check_list = dict()
        for word in t:
            check_list[word] = 0
        print(sum(check_list))


Solution().minWindow(s = "ADOBECODEBANC", t = "ABC")