def solution(n, times):
    answer = 0
    times = sorted(times)
    start, end, current_time = 0, times[0] * n, times[0] * n 
    while start < end:
        available = sum(map(lambda e: current_time // e ,times))
        available_start = sum(map(lambda e: start // e ,times))
        available_end = sum(map(lambda e: end // e ,times))
        if available_end < n:
            current_time, end = current_time + 1, end + 1
        if available > n:
            current_time, end = (start + current_time) // 2, current_time - 1
        elif available < n:
            start, current_time = current_time, (current_time + end) // 2   
        else:

            if available_start == available_end:
                break
            else:
                if available_start < available:
                    start = current_time
                if available < available_end:
                    end = current_time

    answer = current_time
    print(answer)
    return answer

solution(6, [7, 10] )