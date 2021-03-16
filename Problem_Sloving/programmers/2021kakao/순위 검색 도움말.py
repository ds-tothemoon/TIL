def solution(info, query):
    def binary_search(score, score_condition):
        s = 0
        e = len(score) - 1
        while s < e:
            mid = (s + e) // 2
            if (score[mid] < score_condition):
                s = mid + 1
            else:
                e = mid
        return s

    answer = []
    language = dict({'cpp': [], 'java': [], 'python': []})
    stack = dict({'backend': [], 'frontend': []})
    age = dict({'junior': [], 'senior': []})
    soulfood = dict({'pizza' : [], 'chicken': []})
    score = []
    for i in range(len(info)):
        temp = info[i].split()
        language[temp[0]].append(i)
        stack[temp[1]].append(i)
        age[temp[2]].append(i)
        soulfood[temp[3]].append(i)
        score.append((int(temp[4]),i))
    score.sort()
    extracted_score = list(map(lambda item: item[0], score))
    extracted_score_idx = list(map(lambda item: item[1], score))
    for i in range(len(query)):
        LANGUAGE_ORDER = 0
        STACK_ORDER = 2
        AGE_ORDER = 4
        SOULFOOD_ORDER = 6
        SOCRE_ORDER = 7
        ALL = '-'
        temp_query = query[i].split()
        temp_result = set()
        res = 0
        # first condition
        if temp_query[LANGUAGE_ORDER] == ALL:
            for values in language.values():
                temp_result.update(values)
        else:
            temp_result.update(language[temp_query[LANGUAGE_ORDER]])
        
        # second condition
        if temp_query[STACK_ORDER] == ALL:
            pass
        else:
            temp_result = temp_result & set(stack[temp_query[STACK_ORDER]])
        
        # third condition
        if temp_query[AGE_ORDER] == ALL:
            pass
        else:
            temp_result = temp_result & set(age[temp_query[AGE_ORDER]])
        
        # fourth condition
        if temp_query[SOULFOOD_ORDER] == ALL:
            pass
        else:
            temp_result = temp_result & set(soulfood[temp_query[SOULFOOD_ORDER]])
        
        # fifth condition
        score_condition = temp_query[SOCRE_ORDER]
        if score_condition == '-':
            pass
        else:
            score_condition = int(score_condition)
            key = binary_search(extracted_score, score_condition)
            if key >= len(extracted_score):
                temp_result = {}
            else:
                temp_result = temp_result & set(extracted_score_idx[key:])

        answer.append(len(temp_result))
    return answer


solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])