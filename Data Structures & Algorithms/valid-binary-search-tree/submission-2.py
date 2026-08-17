# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, mn, mx):
            if not root:
                return True
            
            if root.val >= mx or root.val <= mn: 
                return False
            else:
                return (dfs(root.left, mn, root.val) and dfs(root.right, root.val, mx))
                
                
        return dfs(root, float("-inf"), float("inf"))