class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def in_boundary(i, j, board):
            if i >=0 and i < len(board) and j >= 0 and j < len(board[i]): return True
            return False

        def rec(board, visited, word, cur, i, j, directions):
            # base case 
            if cur == len(word): 
                return True
            else:
                if in_boundary(i, j, board) and not visited[i][j] and board[i][j] == word[cur]:
                    visited[i][j] = True
                    for dx, dy in directions: 
                        if rec(board, visited, word, cur+1, i + dx, j + dy, directions): 
                            return True
                    visited[i][j] = False
                return False

        
        visited = []
        for i in range(len(board)):
            vis_row = []
            for j in range(len(board[0])):
                vis_row.append(False)
            visited.append(vis_row)
        
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if rec(board, visited, word, 0, i, j, directions):
                    return True
        
        return False
        
