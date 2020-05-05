class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        adjList = [[] for _ in range(N)]
        visited = [False for _ in range(N)]
        grouping = [False for _ in range(N)]
        
        for dislike in dislikes:
            a = dislike[0] - 1
            b = dislike[1] - 1
            adjList[a].append(b)
            adjList[b].append(a)
        
        for i in range(len(adjList)):
            if not visited[i]:
                visited[i] = True
                res = self.is_bipartition(i, adjList, visited, grouping)
            if not res: return False
            
        return True
    def is_bipartition(self, cur, adjList, visited, grouping):
        
        for next in adjList[cur]:
            if not visited[next]:
                visited[next] = True
                grouping[next] = not grouping[cur]
                res = self.is_bipartition(next, adjList, visited, grouping)
                if not res: 
                    return False
            elif grouping[next] == grouping[cur]:
                return False
        return True
            