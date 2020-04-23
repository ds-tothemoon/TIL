class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == [] : return []
        
        MAX_LEN_ROW = len(matrix)
        MAX_LEN_COL = len(matrix[0])
        visited = [[False for _ in range(MAX_LEN_COL)] for _ in range(MAX_LEN_ROW)]
        count = 1
        ret = []
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        idx = 0
        i = 0
        j = 0
        visited[0][0] = True
        ret.append(matrix[0][0])
        
        while count < MAX_LEN_COL * MAX_LEN_ROW:

            if 0<=  i + dx[idx] < MAX_LEN_COL and \
               0<= j + dy[idx] < MAX_LEN_ROW and \
                visited[j + dy[idx]][i + dx[idx]] == False:
                i = i + dx[idx]
                j = j + dy[idx]
                visited[j][i] = True
                count += 1
                ret.append(matrix[j][i])               
            else:                
                idx = (idx + 1 ) % 4
        return ret

print(Solution().spiralOrder(
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

))