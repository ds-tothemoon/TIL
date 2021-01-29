class Solution(object):
    def getSmallestString(self, n, k):
        MAX_VALUE = 25
        get_lowercase_character = lambda x: chr(x + ord('a') - 1)
        num_list = [1 for _ in range(n)]
        remains = k - n

        for i in range(len(num_list)):
            if remains <= 0:
                break
            if remains < MAX_VALUE:
                num_list[i] += remains
                remains = 0
            else:
                num_list[i] += MAX_VALUE
                remains -= MAX_VALUE

        return ''.join(map(get_lowercase_character, reversed(num_list)))

Solution().getSmallestString(5,73)