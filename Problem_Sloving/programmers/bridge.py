root = []
def solution(n, costs):
    global root
    answer = 0
    
    costs = sorted(costs,key=lambda e: (e[2],e[0],e[1]))
    root = [i for i in range(n)]
    
    for cost in costs:
        x = find(cost[0])
        y = find(cost[1])
        if x != y:
            union(x, y)
            answer += cost[2]
    return answer

def find(x):
    global root
    if (root[x] == x):
        return x

    return find(root[x])


def union(x, y):
    global root
    x = find(x)
    y = find(y)
    root[y] = x

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

solution(n,costs)