class Solution:
    
    def traverse_block(self, board, x, y):
        seen = set()
        for i in range(x, x+3): 
            for j in range(y, y+3): 
                if board[i][j] != ".":
                    if board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # traverse rows 
        for i in range (9): 
            seen = set()
            for j in range(9): 
                if board[i][j] != ".":
                    if board[i][j] in seen:
                        return False
                    else: 
                        seen.add(board[i][j])
        print("rows good")
        
        # traverse columns 
        for i in range (9): 
            seen = set()
            for j in range(9): 
                if board[j][i] != ".":
                    if board[j][i] in seen:
                        return False
                    else: 
                        seen.add(board[j][i])
        print("cols good")
        
        # traverse 3x3 blocks 
        for i in range(0, 9, 3): 
            for j in range(0, 9, 3): 
                print (str(i) + " " + str(j))
                print (self.traverse_block(board, i, j))
                if self.traverse_block(board, i, j) != True: 
                    return False
        print("blocks good")

        return True
