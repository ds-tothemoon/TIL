class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        counter = Counter(s)
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1


print(Solution().firstUniqChar("leetcode"))