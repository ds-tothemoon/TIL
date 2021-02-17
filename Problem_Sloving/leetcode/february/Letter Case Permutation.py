class Solution(object):
    res = []
    numbers = '0123456789'
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def dfs(cur_word, location, S):
            if len(S) == location:
                self.res.append(cur_word)
                return
            if S[location] in self.numbers:
                dfs(cur_word + S[location], location + 1, S)
            else:
                dfs(cur_word + S[location].lower(), location + 1, S)
                dfs(cur_word + S[location].upper(), location + 1, S)
        
        dfs('', 0, S)
        return self.res

Solution().letterCasePermutation("ABCDABCDABCD")
                

        