class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        idx = 0
        missing_arr = set([i for i in range(1,1001)]) - set(arr)
        sorted_missing_arr = sorted(list(missing_arr))
        for _ in sorted_missing_arr:
            if idx < k:
                idx += 1
            elif idx == k:
                break
        return sorted_missing_arr[idx-1]

print(Solution().findKthPositive([2,3,4,5],5))
