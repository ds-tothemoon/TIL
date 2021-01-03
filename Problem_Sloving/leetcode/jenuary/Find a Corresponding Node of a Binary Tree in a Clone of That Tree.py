# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """

        return self.traverseNode(original, cloned, target)
        
    
    def traverseNode(self, cur_original, cur_cloned, target):
        ans1 = None
        ans2 = None
        if cur_original == target:
            return cur_cloned
        if cur_original.left:
            ans1 = self.traverseNode(cur_original.left, cur_cloned.left, target)
        if cur_original.right:
            ans2 = self.traverseNode(cur_original.right, cur_cloned.right, target)
        return ans1 or ans2