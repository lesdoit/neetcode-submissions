class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        
        row = [-1] * n
        col = [-1] * m
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[j] = 0
                    col[i] = 0
        
        for i, _ in enumerate(row):
            if row[i] == 0:
                for j in range(m):
                    matrix[j][i] = 0
        
        for i, _ in enumerate(col):
            if col[i] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        
