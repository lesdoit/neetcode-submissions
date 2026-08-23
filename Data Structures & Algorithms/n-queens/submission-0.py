class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Hash sets to track our core invariants in O(1) time
        cols = set()
        posDiag = set()  # Tracks r + c
        negDiag = set()  # Tracks r - c
        
        res = []
        # Initialize an empty N x N board
        board = [["."] * n for _ in range(n)]
        
        def backtrack(r: int):
            # Base Case: If we've successfully placed a queen in every row
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            # Try placing a queen in every column of the current row 'r'
            for c in range(n):
                # If the cell violates any invariant, skip it
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                # 1. Place the queen and update constraints
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                
                # 2. Recurse to the next row (Macro-State Transition)
                backtrack(r + 1)
                
                # 3. Backtrack: Remove the queen and clear constraints
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
                
        # Start the recursion at row 0
        backtrack(0)
        return res