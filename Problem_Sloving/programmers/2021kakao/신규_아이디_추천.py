'''
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
'''

def solution(new_id):
    import re
    def step01_to_lowercase(new_id):
        return new_id.lower()
    def step02_trim_character(new_id):
        return re.sub("[^a-z0-9-_.]","", new_id)
    def step03_trim_double_comma(new_id):
        return re.sub("\.+",".", new_id)
    def step04_trim_edge_comma(new_id):
        return re.sub("(^\.|\.$)","", new_id)
    def step05_fill_empty_id(new_id):
        FILL_WORD = "a"
        if new_id == "":
            return FILL_WORD
        else:
            return new_id
    def step06_trim_long_id(new_id):
        temp = new_id[:15]
        return re.sub("\.$","", temp)
    def step07_fill_small_id(new_id):
        word_length = len(new_id)
        if word_length <= 2:
            return new_id + (new_id[-1] * (3 - word_length))
        return new_id

    temp = new_id
    temp = step01_to_lowercase(temp)
    temp = step02_trim_character(temp)
    temp = step03_trim_double_comma(temp)
    temp = step04_trim_edge_comma(temp)
    temp = step05_fill_empty_id(temp)
    temp = step06_trim_long_id(temp)
    temp = step07_fill_small_id(temp)
    answer = temp
    return answer

solution(".......!@BaT#*......y.ac234def.g.hijk...l")
solution(".")