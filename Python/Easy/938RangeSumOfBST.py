# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root == None:
            return 0
        
        def dfs(root):
            
            if root == None:
                return 0
            if root.val < L or root.val > R:
                return dfs(root.left)+dfs(root.right)+0
            
            return dfs(root.left)+dfs(root.right)+root.val
    
        return dfs(root)