import heapq
'''
최소 힙
heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)

print(heap[0]) 가장 작은 수에 접근
print(heapq.heappop(heap))
print(heap[0])
print(heapq.heappop(heap))
print(heap[0])
print(heapq.heappop(heap))
print(heap[0])
print(heap)
'''
'''
최대 힙
튜플 입력시 맨 앞에 있는 값을 기준으로 정렬 즉, 우선순위를 준다

nums =  [4, 1, 7, 3, 8, 5]
heap = []
for num in nums:
  heapq.heappush(heap, (-num, num))

while heap:
  print(heapq.heappop(heap)[1])

'''

'''
k번째 최소값

def kth_smallest(nums, k):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)
  
  kth_min = None
  
  for i in range(k):
    kth_min = heapq.heappop(heap)
  
  return kth_min

print(kth_smallest([4, 1, 7, 3, 8, 5], 3))
'''
'''
힙 정렬
def heap_sort(nums):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)
  
  sorted_nums = []
  while heap:
    sorted_nums.append(heapq.heappop(heap))
  return sorted_nums

print(heap_sort([4, 1, 7, 3, 8, 5]))
'''   

