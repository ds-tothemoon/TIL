def solution(lines):
    answer = 0
    trans_lines = list(map(trans_milli_second, lines))
    milli_second_for_range = 999
    gikun_keys = sorted(sum(trans_lines,[]))
    for gikun_key in gikun_keys:
        temp_value = 0
        for i in range(len(trans_lines)):
            start = trans_lines[i][0] 
            end = trans_lines[i][1]
            if  end < gikun_key or gikun_key + milli_second_for_range < start:
                pass
            else:
                temp_value += 1
        answer = max(answer, temp_value)
    return answer


def trans_milli_second(line):
    line_split = line.split(' ')[1:]
    time_part = list(map(float,line_split[0].split(':')))
    range_part = float(line_split[1][:-1])
    second_weight = 1000
    minute_weight = 60 * second_weight
    hour_weight = 60 * minute_weight
    target = time_part[0] * hour_weight \
            + time_part[1] * minute_weight \
            + time_part[2] * second_weight
    result = [int(target - range_part * second_weight + 1),int(target)]
    return result


solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"

])

solution(	[
    "2016-09-15 01:00:04.001 2.0s", 
    "2016-09-15 01:00:07.000 2s"
    ])