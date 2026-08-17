# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        result = []
        def dfs(root, seen):
            if not root:
                return
            
            good = True
            for i in range(len(seen)):
                if seen[i] > root.val:
                    good = False
                    break
            
            if good:
                result.append(root.val)
            
            dfs(root.left, seen + [root.val])
            dfs(root.right, seen + [root.val])
        
        dfs(root, [])
        return len(result)