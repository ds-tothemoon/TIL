# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        def traverse_child(node, depth):
            if not node: return

            traverse_child(node.left, depth + 1)
            if node:
                temp[depth] = node.val
            traverse_child(node.right, depth + 1)
        
        temp = dict()
        res = []
        traverse_child(root, 0)
        for e in sorted(temp.keys()):
            res.append(temp[e])
        return res