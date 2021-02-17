class Solution(object):
    def shiftingLetters(self, S, shifts):
        res = ""
        alphabet_count = ord("z")-ord("a") + 1
        
        for i in range(len(shifts)-1,0,-1):
            shifts[i-1] += shifts[i]

        for i in range(len(S)):
            res += chr(ord("a") + (ord(S[i]) - ord("a") + shifts[i]) % alphabet_count)
        
        return res

Solution().shiftingLetters(S = "abc", shifts = [3,5,9])