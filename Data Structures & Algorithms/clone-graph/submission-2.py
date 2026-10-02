"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        def dfs(node, visited):
            if node.val in visited: 
                return visited[node.val]
            
            cur = Node(node.val)
            visited[node.val] = cur
            
            for neigh in node.neighbors: 
                cur.neighbors.append(dfs(neigh, visited))
            return cur
            
        if not node: return node
        visited = {}
        ans = dfs(node, visited)
        return ans