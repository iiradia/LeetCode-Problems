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
        def helper(node, parent_node, it_x):
            if node:
                if node.val in [x,y]:
                    x_l.append({'d':it_x, 'p':parent_node})
                    
                helper(node.left, node.val, it_x+1)
                helper(node.right, node.val, it_x+1)
          
        x_l = []
        helper(root, -1, 0)
        return x_l[0]['p'] != x_l[1]['p'] and x_l[0]['d'] == x_l[1]['d']