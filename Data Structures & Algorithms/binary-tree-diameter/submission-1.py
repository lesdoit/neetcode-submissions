# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def __init__(self):
        self.maxdiam = 0
    
    def maxdepth(self, node):
        if not node:
            return 0
        
        leftdepth = self.maxdepth(node.left)
        rightdepth = self.maxdepth(node.right)

        self.maxdiam = max(self.maxdiam, leftdepth+rightdepth)
        
        return max(1 + leftdepth, 1 + rightdepth)
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdepth(root)
        return self.maxdiam

        
        

