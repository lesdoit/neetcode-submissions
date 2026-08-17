# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = float("-inf")
        
        def dfs(root, k, cnt):
            if not root:
                return cnt
            
            cnt = dfs(root.left, k, cnt)
            cnt += 1
            nonlocal ans
            if cnt == k:
                ans = root.val
            cnt = dfs(root.right, k, cnt)
            return cnt
        
        dfs(root, k, 0)
        
        return ans