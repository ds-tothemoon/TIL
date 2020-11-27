'''
스냅챗에서 출제된 문제입니다.

중첩될 수 있는 인터벌들을 갖는 리스트가 있습니다. 중첩되는 인터벌들을 하나로 합친 새로운 리스트를 반환하세요.

입력 리스트는 정렬되어 있지 않습니다.

예를 들어, [(1, 3), (5, 8), (4, 10), (20, 25)] 가 주어지면, [(1, 3), (4, 10), (20, 25)] 를 반환해야 합니다.
'''

def solution(interval):
    sort_interval = sorted(interval,key=lambda x: (x[0],x[1]))
    print(sort_interval)
    new_interval = []
    new_interval.append(sort_interval[0])
    for tmp_interval in sort_interval:
        last_interval = new_interval[-1]
        if last_interval[1] < tmp_interval[0]:
            new_interval.append(tmp_interval)
        else:
            new_interval[-1] = (last_interval[0], max(last_interval[1], tmp_interval[1]))
    print(new_interval)

solution([(1, 3), (5, 8), (4, 10), (20, 25)])