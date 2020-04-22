# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        tmp = 0
        while l1 and l2:
            tmp = l1.val + l2.val + tmp
            if head == None:
                head = ListNode(tmp % 10)
                node = head
            else:
                node.next = ListNode(tmp % 10)
                node = node.next
            l1 = l1.next
            l2 = l2.next
            tmp = tmp // 10
        while l1:
            tmp = l1.val + tmp
            node.next = ListNode(tmp % 10)
            node = node.next
            
            l1 = l1.next
            tmp = tmp // 10
        while l2:
            tmp = l2.val + tmp
            node.next = ListNode(tmp % 10)
            node = node.next
            
            l2 = l2.next
            tmp = tmp // 10
        if tmp != 0:
            node.next = ListNode(tmp % 10)
            node = node.next
        
        return head