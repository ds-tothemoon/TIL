# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        is_same_level = self.find_level(root, 0, x) == self.find_level(root, 0, y)
        is_same_parent = self.check_parent(root, x, y)
        if is_same_level and not is_same_parent:            
            return True
        else:
            return False
        
    def find_level(self, root, level, target):
        if root == None:
            return 0
        elif root.val == target:
            return level
        else:
            return self.find_level(root.left, level + 1, target) + self.find_level(root.right, level + 1, target)       
    def check_parent(self, root, x,y):
        if root == None:
            return False
        if root.left != None and root.right != None:
            if root.left.val == x and root.right.val == y:
                return True
            elif root.left.val == y and root.right.val == x:
                return True
        return self.check_parent(root.left, x,y) or self.check_parent(root.right, x,y)
            