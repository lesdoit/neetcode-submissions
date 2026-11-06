class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Kahn's topological sort approach 
        # create a graph. Connect a directed edge from node1 to node2 if
        # node1.val < node2.val 
        # run kahn's on that graph 
        n, m = len(matrix), len(matrix[0])
        adj = [[] for _ in range(m*n)]
        indeg = [0] * (m*n)
        
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        def in_boundary(i, j):
            if i<0 or i>=n or j<0 or j>=m: return False 
            return True

        def create():
            for i in range(n):
                for j in range(m):
                    node_idx = (i * m) + j
                    for dx, dy in dirs: 
                        if in_boundary(i+dx, j+dy) and matrix[i+dx][j+dy] > matrix[i][j]:
                            adj[node_idx].append((i+dx)*m + (j+dy))
                            indeg[(i+dx)*m + (j+dy)] += 1
        
        def kahns():
            q = collections.deque()
            for idx, ind in enumerate(indeg):
                if ind == 0:
                    q.append((idx, 1))      # second param is the length of LIP
            ans = 0
            while q: 
                idx, lip = q.popleft()
                ans = max(ans, lip)
                for nei in adj[idx]:
                    indeg[nei]-=1
                    if not indeg[nei]:
                        q.append((nei, 1 + lip))
            return ans
        create()
        return kahns()
        
