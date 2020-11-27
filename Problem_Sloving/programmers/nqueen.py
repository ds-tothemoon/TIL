answer = 0
def solution(n):
    global answer
    for i in range(n):
        traverse([i], n)
    print(answer)
    return answer

def traverse(queen_position, n):
    if len(queen_position) == n:
        global answer
        answer += 1
        return
    available = [1 for _ in range(n)]
    difference = len(queen_position)
    for i in range(len(queen_position)):
        available[queen_position[i]] = 0
        
        if queen_position[i] - difference >= 0:
            available[queen_position[i]-difference] = 0    
        
        if queen_position[i] + difference < n:
            available[queen_position[i]+difference] = 0

        difference -= 1
    for i in range(len(available)):
        if available[i]:
            queen_position.append(i)
            traverse(queen_position, n)
            queen_position.pop()

solution(4)