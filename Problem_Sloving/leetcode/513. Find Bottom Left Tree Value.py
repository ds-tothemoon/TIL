# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    res = [0,0]
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(root, depth):
            if root:
                traverse(root.right, depth + 1)
                if depth >= self.res[0]:
                    self.res = [depth, root.val]
                traverse(root.left, depth + 1)
                
        traverse(root, 0)
        return self.res[1]