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
                return 0, 0
            
            leftdepth, leftdia = dfs(node.left)
            rightdepth, rightdia = dfs(node.right)

            
            dia = max(max(leftdia, rightdia), leftdepth + rightdepth)

            return (max(1 + leftdepth, 1 + rightdepth), dia)
        
        depth, dia = dfs(root)
        return dia

        
        

