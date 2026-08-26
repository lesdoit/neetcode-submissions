class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def deep_copy(board, res):
            board_copy = []
            for row in board:
                row_s = ''.join(row)
                board_copy.append(row_s)
            res.append(board_copy)

        def init_board(n): 
            board = []
            for i in range(n):
                row = ['.' for j in range(n)]
                board.append(row)
            return board

        def check(board, row, col):
            # check column 
            for r in range(row, -1, -1):
                if board[r][col] == 'Q': return False

            # check diagonal (y = x)
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q': return False
                r -= 1
                c -= 1

            # check diagonal
            r, c = row - 1, col + 1
            while r >= 0 and c < len(board): 
                if board[r][c] == 'Q': return False
                r-=1
                c+=1

            return True

        def rec(board, row, n, res):
            # base case 
            if row == n: 
                deep_copy(board, res)
            else: 
                # recurse case 
                for col in range(n):
                    if check(board, row, col):
                        board[row][col] = 'Q'
                        rec(board, row + 1, n, res)
                        board[row][col] = '.'
                    
        res = []
        board = init_board(n)
        rec(board, 0, n, res)
        return res