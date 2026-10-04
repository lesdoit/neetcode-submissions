class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacvisit, atlvisit = set(), set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        m = len(heights)
        n = len(heights[0])

        def in_boundary(r, c):
            if r < 0 or r >= m or c < 0 or c >= n: return False
            return True

        def dfs(r, c, visit):
            if (r, c) in visit: return 
            visit.add((r,c))
            for dr, dc in directions:
                if in_boundary(r+dr, c+dc) and (r+dr, c+dc) not in visit and heights[r+dr][c+dc] >= heights[r][c]: 
                    dfs(r+dr, c+dc, visit)
        
        
        # init reachable to pacific 
        for i in range(n): 
            dfs(0, i, pacvisit)
        
        for i in range(m):
            dfs(i, 0, pacvisit)
        
        # init reachable to atlantic 
        for i in range(n):
            dfs(m-1, i, atlvisit)
        
        for i in range(m):
            dfs(i, n-1, atlvisit)
        
        ans = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacvisit and (i, j) in atlvisit: 
                    ans.append([i, j])
        
        return ans