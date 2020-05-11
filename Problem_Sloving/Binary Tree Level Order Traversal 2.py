# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        q = deque()
        q.append(root)
        ret = []
        answer = []

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                level.append(node.val)
            ret.append(level)
        for i in range(len(ret)-1,-1,-1):
            answer.append(ret[i])
        print(ret)
        print(answer)
        return answer

head = TreeNode(3)
head.left = TreeNode(9)
head.right = TreeNode(20)
head.right.left = TreeNode(15)
head.right.right = TreeNode(7)

Solution().levelOrderBottom(head)