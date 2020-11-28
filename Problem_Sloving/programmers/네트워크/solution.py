def solution(n, computers):
    from collections import deque
    answer = 0
    step = 1
    visited_network = [[0 for _ in range(n)] for _ in range(n)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(n):
        for j in range(n):
            if visited_network[i][j] == 0:
                queue = deque([i,j])
                visited_network[i][j] = step
                while queue:
                    current_val = queue.popleft()
                    for k in range(4):
                        x = current_val + dx[k]
                        y = current_val + dy[k]
                        if 0 <= x < n and 0 <= y < n:
                            if visited_network[x][y] == 0:
                                visited_network[x][y] = step
                step += 1
    print(visited_network)
    return answer

solution(3, [
    [1, 1, 0], 
    [1, 1, 0], 
    [0, 0, 1]])