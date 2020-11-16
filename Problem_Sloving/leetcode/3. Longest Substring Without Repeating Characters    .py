def lengthOfLongestSubstring(self, s: str) -> int:
    ans, subStrStart, char = 0, 0, {}
    for i in range(len(s)):
        if not (char.get(s[i]) is None):
            while s[subStrStart] != s[i]:
                if not (char.get(s[subStrStart]) is None): del char[s[subStrStart]]
                subStrStart += 1
            subStrStart += 1
        char[s[i]] = i
        ans = max(ans, i - subStrStart +1)
    return ans