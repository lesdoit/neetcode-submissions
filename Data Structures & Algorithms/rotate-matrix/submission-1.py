class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for layer in range(n, n//2, -1):
            # derive top left corner based on layer 
            r, c = n - layer, n - layer
            sidelen = n - ((n-layer)*2)
            
            for i in range(sidelen-1):
                tl = matrix[r][c+i]
                tr = matrix[r+i][c+sidelen-1]
                br = matrix[r+sidelen-1][c+sidelen-i-1]
                bl = matrix[r+sidelen-i-1][c]

                matrix[r+i][c+sidelen-1] = tl
                matrix[r+sidelen-1][c+sidelen-i-1] = tr
                matrix[r+sidelen-i-1][c] = br
                matrix[r][c+i] = bl