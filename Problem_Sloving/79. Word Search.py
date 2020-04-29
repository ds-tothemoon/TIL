class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        start = []
        MAX_ROW = len(board)
        MAX_COL = len(board[0])
        for i in range(MAX_ROW):
            for j in range(MAX_COL):
                if board[i][j] == word[0]:
                    start.append((i,j,1))
        for i in range(len(start)):
            if len(word) == 1:
                return True
            if self.bfs(start[i], board, word):
                return True
        return False
   
    def bfs(self, start, board, word):
        from collections import deque
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        queue = deque()
        MAX_ROW = len(board)
        MAX_COL = len(board[0])
        visited = [[False for _ in range(MAX_COL)] for _ in range(MAX_ROW)]
        queue.append(start)
        visited[start[0]][start[1]] = True
        while queue:
            ny,nx,order = queue.popleft()
            if order < len(word):
                for i in range(4):
                    if 0 <= ny + dy[i] < MAX_ROW and \
                       0 <= nx + dx[i] < MAX_COL and \
                       visited[ny + dy[i]][nx + dx[i]] == False:
                        if board[ny + dy[i]][nx + dx[i]] == word[order]:
                            print(ny + dy[i],nx + dx[i], order ,word[order])
                            if order == len(word) - 1:
                                return True
                            else:
                                queue.append((ny + dy[i],nx + dx[i], order + 1))
                                visited[ny + dy[i]][nx + dx[i]] = True
        return False

print(Solution().exist(
[
    ["A","B","C","E"],
    ["S","F","E","S"],
    ["A","D","E","E"]
],
"ABCESEEEFS"
))