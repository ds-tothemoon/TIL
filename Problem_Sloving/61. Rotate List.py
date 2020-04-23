#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        count = self.calculate_len(head)

        for _ in range(k % count):
            head = self.rotate(head)
        return head
    
    def rotate(self,head):
        cur_node = head.next
        val = head.val
        while cur_node:
            val, cur_node.val = cur_node.val, val
            cur_node = cur_node.next
        head.val = val
        return head

    def calculate_len(self, head):
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        return count
