def solution(key, lock):
    answer = True
    N = len(key)
    key_index = []
    empty_index = []
    for i in range(N):
        for j in range(N):
            if key[i][j]: 
                key_index.append([i,j])
            if not lock[i][j]: 
                empty_index.append([i,j])
    print(key_index)
    print(empty_index)
    for i in range(len(key_index)):
        standard = empty_index[i]
        x_diff = key_index[i][0] - empty_index[0][0]
        y_diff = key_index[i][1] - empty_index[0][1]
        tmp_key_idx = list(map(lambda x: [x[0]-x_diff,x[1]-y_diff],key_index))
                        
    return answer
solution([
    [0, 0, 0], 
    [1, 0, 0], 
    [0, 1, 1]
    ],[
    [1, 1, 1], 
    [1, 1, 0], 
    [1, 0, 1]
    ])