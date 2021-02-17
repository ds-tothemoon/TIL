class Solution(object):
    def findClosestElements(self, arr, k, x):
        return sorted(sorted(arr, key=lambda p: abs(p-x))[:k])
