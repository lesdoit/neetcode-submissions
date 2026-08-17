# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        subtree = False
        def dfs(p, q):
            nonlocal subtree
            
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                if isSameTree(p, q):
                    subtree = True
            if p:
                dfs(p.left, q)
                dfs(p.right, q)

        def isSameTree(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            else:
                return False
        
        dfs(root, subRoot)
        return subtree