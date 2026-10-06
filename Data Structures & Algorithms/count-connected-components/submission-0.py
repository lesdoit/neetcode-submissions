
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        adj = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(node):
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]: dfs(nei)

        ans = 0
        for i in range(len(adj)):
            if not visited[i]:
                ans += 1
                dfs(i)
        
        return ans 