class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        res = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        res[0][0] = grid[0][0]

        for i in range(m):
          for j in range(n):
            if i == 0 and j == 0:
              continue
            else:
              if i == 0 and j != 0:
                res[i][j] =  res[i][j-1] + grid[i][j]
              elif i != 0 and j == 0:
                res[i][j] =  res[i-1][j] + grid[i][j]
              else:
                res[i][j] = min(res[i-1][j], res[i][j-1]) + grid[i][j]
        return res[m-1][n-1]
