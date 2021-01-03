import functools

class Solution(object):
    def canFormArray(self, arr, pieces):    
        answer = True
        visited = [False for _ in range(len(arr))]
        for piece in pieces:
            # print(piece, visited, arr)
            try:
                start_idx = arr.index(piece[0])
                cmp_arr = arr[start_idx:start_idx+len(piece)]
                if functools.reduce(lambda i, j : i and j, 
                    map(lambda m, k: m == k, cmp_arr, piece), True):
                    visited[start_idx:start_idx+len(piece)] = [True for _ in range(len(piece))]
            except ValueError:
                answer = False
                break
        if sum(visited) != len(visited):
            answer = False
        return answer

# class Solution2(object):
#     def canFormArray(self, arr, pieces):
#         """
#         :type arr: List[int]
#         :type pieces: List[List[int]]
#         :rtype: bool
#         """
#         ans1 = self.calculate(arr, pieces)
#         ans2 = self.calculate(arr, pieces[::-1])
#         if ans1 or ans2:
#             return True
#         else:
#             return False
#     def calculate(self, arr, pieces):
#         answer = []
#         cur_idx = 0
        
#         for piece in pieces:
#             tmp = answer + piece
#             tmp2 = answer + piece[::-1]
#             if functools.reduce(lambda i, j : i and j, 
#                 map(lambda m, k: m == k, arr[:len(tmp)], tmp), True):
#                 answer = tmp
#                 pass
#             elif functools.reduce(lambda i, j : i and j, 
#                 map(lambda m, k: m == k, arr[:len(tmp2)], tmp2), True):
#                 answer = tmp2
#                 pass
#             else:
#                 break
#         if functools.reduce(lambda i, j : i and j, 
#                 map(lambda m, k: m == k, arr, answer), True):
#             print(answer, arr, True)
#             return True
#         else:
#             return False
        
print(Solution().canFormArray(arr = [85], pieces = [[85]]))
print(Solution().canFormArray(arr = [15,88], pieces = [[88],[15]]))
print(Solution().canFormArray(arr = [49,18,16], pieces = [[16,18,49]]))
print(Solution().canFormArray([91,4,64,78], [[78],[4,64],[91]]))
print(Solution().canFormArray([1,3,5,7], pieces = [[2,4,6,8]]))
