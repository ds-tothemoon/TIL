class Solution(object):
    def ladderLength(self, begin_word, end_word, word_list):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        return self.bfs(begin_word, end_word, word_list)

    def bfs(self,  begin_word, end_word, word_list):
        from collections import deque
        queue = deque()
        queue.append((begin_word, []))
        while queue:
            cur_word, sequence = queue.popleft()
            for i in range(len(word_list)):
                if self.is_next(cur_word, word_list[i]) and word_list[i] not in sequence:
                    if end_word == word_list[i]:
                        print(sequence)
                        return len(sequence) + 2 
                    else : queue.append((word_list[i], sequence + [word_list[i]]))
        return 0

    def is_next(self, word1, word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
        if count == 1:
            return True
        else:
            return False

Solution().ladderLength("red",
"tax",
["ted","tex","red","tax","tad","den","rex","pee"])