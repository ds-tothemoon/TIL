# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        if root == None : return 0
        q = deque()
        level = 0
        q.append(root)
        
        while q:
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left != None: q.append(node.left)
                if node.right != None: q.append(node.right)
            
        
        return level
                