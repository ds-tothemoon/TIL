'''
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
'''

def solution(p):
    answer = make_string(p)
    return answer

def make_string(p):
    # 1st condition
    if p == '':
        return ''
    # 2nd condition
    u,v = divide_balanced_string(p)
    # 3rd condition
    if check_right_string(u):
        u += make_string(v)
    else:
        u = make_right_string(u, v)
    return u

def make_right_string(u, v):
    p = '('
    p += make_string(v)
    p += ')'
    if len(u) >= 2:
        for i in range(1,len(u)-1):
            if u[i] == '(':
                p+= ')'
            else:
                p+= '('
    return p

def check_right_string(p):
    left = 0
    for i in range(len(p)):
        if p[i] == '(': left += 1
        else:
            if left == 0: 
                return False
            else:
                left -= 1
    return True

def divide_balanced_string(p):
    if len(p) == 0:
        return '', ''
    u = ''
    v = ''
    counter = {'(':0, ')':0}
    counter[p[0]] = 1
    for i in range(1, len(p)):
        counter[p[i]] += 1
        if counter['('] == counter[')']:
            u = p[:i+1]
            v = p[i+1:]
            break
    return u,v
solution('()))((()')