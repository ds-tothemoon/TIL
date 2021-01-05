# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = 0
        num_set = set()
        distinct_list = []
        cur_node = head
        
        
        while cur_node:
            num_set.add(cur_node.val)
            if tmp != len(num_set):
                distinct_list.append(cur_node.val)
            else:
                if len(distinct_list) > 0 and distinct_list[-1] == cur_node.val:
                    distinct_list.pop()
            cur_node = cur_node.next
            tmp = len(num_set)
            
        if not distinct_list: 
            return None
        
        head = ListNode()
        cur_node = head
        for i in range(len(distinct_list)):
            cur_node.val = distinct_list[i]
            if i < len(distinct_list) - 1:
                cur_node.next = ListNode()
                cur_node = cur_node.next
        return head