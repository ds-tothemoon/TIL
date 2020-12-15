def solution(words, queries):
    import re
    tmp = 'Z'.join(words) + 'Z'
    new_queries = list(map(lambda s: str(s).replace('?','[a-z]')+'Z', queries))
    answer = list(map(lambda query: len(re.compile(query).findall(tmp)), new_queries))
    return answer

solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
["fro??", "????o", "fr???", "fro???", "pro?"]
)