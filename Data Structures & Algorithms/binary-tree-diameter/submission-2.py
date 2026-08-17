# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam = 0

        def dfs(node):
            if not node:
                return 0
            
            leftdepth = dfs(node.left)
            rightdepth = dfs(node.right)

            nonlocal max_diam
            max_diam = max(max_diam, leftdepth + rightdepth)

            return max(1 + leftdepth, 1 + rightdepth)
        
        dfs(root)
        return max_diam

        
        

