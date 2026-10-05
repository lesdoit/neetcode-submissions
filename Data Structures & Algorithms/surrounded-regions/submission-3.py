class Solution:
    def solve(self, board: List[List[str]]) -> None:
        edgevisited = set()
        insidevisited = set()
        
        m = len(board)
        n = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def in_boundary(r, c):
            if r<0 or r>=m or c<0 or c>=n: return False
            return True

        def dfs(r, c, visited):
            if not in_boundary(r, c) or (r, c) in visited or board[r][c] != "O":
                return
            visited.add((r,c))
            for dr, dc in directions: 
                dfs(r+dr, c+dc, visited)
        
        # init dfs from edges of the matrix 
        for i in range(m):
            dfs(i, 0, edgevisited)
            dfs(i, n-1, edgevisited)
        
        for i in range(n):
            dfs(0, i, edgevisited)
            dfs(m-1, i, edgevisited)
        
        print(f"EV: {edgevisited}")

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in edgevisited:
                    board[i][j] = 'X'
        
