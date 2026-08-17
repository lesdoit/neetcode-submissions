# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        result = []
        def dfs(root, maxseen):
            if not root:
                return
            
            if root.val >= maxseen:
                result.append(root.val)
            maxseen = max(maxseen, root.val)
            
            dfs(root.left, maxseen)
            dfs(root.right, maxseen)
        
        dfs(root, float("-inf"))
        print(result)
        return len(result)