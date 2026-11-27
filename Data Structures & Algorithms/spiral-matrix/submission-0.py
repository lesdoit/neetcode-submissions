class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        r, c = 0, 0
        res = []
        
        while m>0 and n>0:
            
            # top row 
            for i in range(n):
                res.append(matrix[r][c+i])
            
            # right col 
            for i in range(1, m):
                res.append(matrix[r+i][c+n-1])
            
            if m > 1:
                # bottom row
                for i in range(n-2, -1, -1):
                    res.append(matrix[r+m-1][c+i])
            
            if n > 1: 
                # left column 
                for i in range(m-2, 0, -1):
                    res.append(matrix[r+i][c])
            
            r+=1
            c+=1
            m-=2
            n-=2
        return res