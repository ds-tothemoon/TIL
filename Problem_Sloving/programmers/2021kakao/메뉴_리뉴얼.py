def solution(orders, course):
    from itertools import combinations
    res = []
    course_counters = [dict() for _ in range(len(course))] 
    for order in orders:
        for i in range(len(course)):
            if len(order) >= course[i]:
                for combination in combinations(order, course[i]):
                    key = ''.join(sorted(combination))
                    temp = course_counters[i].get(key, 0)
                    course_counters[i][key] = temp + 1

    for course_counter in course_counters:
        temp_list = []
        MAX_ORDER = -1
        for key, value in course_counter.items():
            temp = [key,value]
            MAX_ORDER = max(MAX_ORDER, value)
            temp_list.append(temp)
        for item in temp_list:
            if item[1] == MAX_ORDER and MAX_ORDER > 1:
                res.append(item[0])
    res.sort()
    
    return res

# solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])
#solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5])
solution(["XYZ", "XWY", "WXA"], [2, 3, 4])