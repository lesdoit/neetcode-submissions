class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # any acyclic graph is a tree
        # detect a cycle in undirected graph. Return false if there is, true otherwise 

        # detect cycle via dfs using 3-numbered visited state  
        # 0 - unvisited, 1 - visiting, 2 - fully explored
        
        if len(edges) > (n-1): return False

        visited = [0] * n
        adj = [[] for i in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()
        
        def dfs(node, parent):
            if node in visited: 
                return False
            
            visited.add(node)
            for neigh in adj[node]:
                if neigh != parent:
                    if not dfs(neigh, node):
                        return False
            return True
        
        return dfs(0, -1) and len(visited) == n

        
        
        
