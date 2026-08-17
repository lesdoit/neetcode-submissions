class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        n = R * C 

        # row = mid / c 
        # col = mid % r
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = lo + (hi - lo)//2
            r = mid//C
            c = mid%C 
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return False
