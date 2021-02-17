class Solution(object):
    def printVertically(self, s):
        words = s.split()
        MAX_VALUE = 0 
        
        for word in words:
            MAX_VALUE = len(word) if MAX_VALUE < len(word) else MAX_VALUE
        
        for i in range(len(words)):
            words[i] += " " * (MAX_VALUE - len(words[i]))
        
        res = ["" for i in range(MAX_VALUE)]
        
        for word in words:
            for i in range(len(word)):
                res[i] += word[i]
        
        res = list(map(lambda word: word.rstrip(),res))
        return res
        
Solution().printVertically("TO BE OR NOT TO BE")