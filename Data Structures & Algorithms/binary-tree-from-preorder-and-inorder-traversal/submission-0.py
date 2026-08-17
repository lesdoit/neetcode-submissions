# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        curr_idx = 0
        
        def dfs(inorder, inorder_idx_map, left, right):
            if left > right: 
                return None
            
            nonlocal curr_idx
            
            root_val = preorder[curr_idx]
            curr_idx += 1
            root = TreeNode(root_val, None, None)
            mid = inorder_idx_map[root_val]
            
            root.left = dfs(inorder, inorder_idx_map, left, mid - 1)
            root.right = dfs(inorder, inorder_idx_map, mid + 1, right)
        
            return root
        
        inorder_idx_map = {val: idx for idx, val in enumerate(inorder)}
        n = len(preorder)
        return dfs(inorder, inorder_idx_map, 0, n-1)