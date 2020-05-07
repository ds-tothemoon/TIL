class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, (-num,num))
        
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.heap, (-val,val))
        sorted_nums = sorted(self.heap, key=lambda x: x[0])
        res = sorted_nums[self.k - 1]
        return res[1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)