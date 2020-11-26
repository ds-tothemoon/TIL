def solution(scoville, K):
    import heapq
    answer = 0
    count = 0
    heapq.heapify(scoville)

    while len(scoville) > 1:
        e1 = heapq.heappop(scoville)
        if e1 >= K:
            break
        e2 = heapq.heappop(scoville)
        heapq.heappush(scoville, e1 + e2 * 2)
        count += 1

    answer = count
    if scoville[0] < K:
        answer = -1
    return answer

solution([1, 2, 3, 9, 10, 12], 7)