class Solution(object):
    def shortestToChar(self, s, c):
        def update_distance(idx):
            distance = 1
            while idx - distance >= 0 and res[idx - distance] != 0:
                res[idx - distance] = min(res[idx - distance], distance)
                distance += 1
            distance = 1
            while idx + distance < len(res) and res[idx + distance] != 0:
                res[idx + distance] = min(res[idx + distance], distance)
                distance += 1


        res = [len(s) for _ in range(len(s))]
        for i in range(len(s)):
            if s[i] == c:
                res[i] = 0
                update_distance(i)
        return res

Solution().shortestToChar(s = "loveleetcode", c = "e")
