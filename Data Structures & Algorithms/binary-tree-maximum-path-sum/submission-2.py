# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float("-inf")
        
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            nonlocal max_path_sum
            max_path_sum = max(max_path_sum, root.val, root.val + left, root.val + right, root.val + left + right)

            return max(root.val, root.val + left, root.val + right)

        dfs(root)
        
        return max_path_sum