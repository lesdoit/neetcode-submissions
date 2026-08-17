# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None: 
            return None
        
        # post order operations 
        # fix left subtree first 
        left = self.invertTree(root.left)

        # then right subtree 
        right = self.invertTree(root.right)

        # then swap left and right subtree pointers 
        tmp = left 
        root.left = right 
        root.right = tmp

        return root
