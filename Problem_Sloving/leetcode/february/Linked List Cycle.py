# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        val = 9999999
        while head:
            if head.val == val: return True
            else:
                head.val = val
                head = head.next
        return False