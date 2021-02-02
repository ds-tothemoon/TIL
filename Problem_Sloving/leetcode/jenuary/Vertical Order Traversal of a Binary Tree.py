# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def verticalTraversal(self, root):
        node_list = []

        self.insert_node_with_location(root , 0, 0, node_list)
        node_list.sort(key=lambda node: (node[1],-node[2], node[0]))
 
        return self.traverse_vertical_order(node_list)
        
    def insert_node_with_location(self, node, x, y, node_list):
        if node.left:
            self.insert_node_with_location(node.left,x-1,y-1, node_list)
        if node.right:
            self.insert_node_with_location(node.right,x+1,y-1, node_list)
        
        node_list.append((node.val,x,y))
    
    def traverse_vertical_order(self, node_list):
        result = []
        cur_x = node_list[0][1]
        cur_node_list = []
        for index, node in enumerate(node_list):
            if cur_x == node[1]:
                cur_node_list.append(node[0])
            else:
                cur_x = node[1]
                result.append(cur_node_list)
                cur_node_list = [node[0]]
            if index == len(node_list) - 1: result.append(cur_node_list)
        return result