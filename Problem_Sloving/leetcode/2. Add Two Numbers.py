# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answer = ListNode()
        cur_node = answer
    
        while l1 or l2:
            tmp = cur_node.val
            
            if l1:
                tmp += l1.val
                l1 = l1.next
            if l2:
                tmp += l2.val
                l2 = l2.next
            
            cur_node.val = tmp % 10
            
            if tmp >= 10:
                cur_node.next = ListNode(1)            
            
            if l1 == None and l2 == None:
                break
            
            if tmp < 10:
                cur_node.next = ListNode()
            
            cur_node = cur_node.next
        
        return answer