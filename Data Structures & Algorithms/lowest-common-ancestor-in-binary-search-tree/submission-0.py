# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # keep traversing down the bst. 
        # if the p and q nodes are in left and right subtrees 
        # rooted at the current node, then the current node is the 
        # least common ancestor 
        p_cmp = 0
        if p.val < root.val:
            p_cmp = -1
        elif p.val > root.val:
            p_cmp = 1
        
        q_cmp = 0
        if q.val < root.val:
            q_cmp = -1 
        elif q.val > root.val:
            q_cmp = 1
        
        if p_cmp != q_cmp:
            return root
        if p_cmp == -1: 
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
        