# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # keep traversing down the bst. 
        # if the p and q nodes are both in left or right subtree, then
        # recursively call that tree and pass p and q
        # if p and q are not both on the left or right, then current node is 
        # lca 

        if not root or not p or not q:
            return None
        
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q) 
        else:
            return root
        
        