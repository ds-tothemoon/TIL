def solution(priorities, location):
    from collections import deque
    printed_list = []
    printing_list = deque()
    for idx, val in enumerate(priorities):
        printing_list.append((val,idx))
    
    while printing_list:
        cur_page = printing_list.popleft()
        is_printed = True
        for next_page in printing_list:
            if next_page[0] > cur_page[0]:
                printing_list.append(cur_page)
                is_printed = False
                break
        if is_printed:
            printed_list.append(cur_page[1]
            
    return printed_list.index(location)+1
        

solution([1,1,9,1,1,1], 0)
solution([2,1,3,2], 2)
