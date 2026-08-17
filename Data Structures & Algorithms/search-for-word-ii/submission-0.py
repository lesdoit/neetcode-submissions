class Solution:

    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)      # number of rows
        n = len(board[0])   # number of cols

        # function to return an empty matrix for marking visited nodes 
        def get_empty_visited(m, n):
            return [[0]*n for i in range(m)]

        # direction array for looping over the four directions 
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        # dfs function to traverse in the four directions 
        def dfs(r, c, word_sub, visited):
            # base condition - word found 
            if len(word_sub) == 0:
                return True
            
            # boundary check
            if (not (0 <= r < m)) or (not (0 <= c < n)) :
                return False
            
            # visited check 
            if visited[r][c] == 1:
                return False

            if board[r][c] == word_sub[0]:
                visited[r][c] = 1
                for d in directions:
                    if dfs(r + d[0], c + d[1], word_sub[1:], visited):
                        return True
                visited[r][c] = 0
            return False
        

        # create a map of letters to indices to decide the starting location of from which 
        # to start the dfs 
        idx_mp = defaultdict(list)
        for i in range(m):
            for j in range(n):
                idx_mp[board[i][j]].append((i,j))
        
        ans = []
        for word in words:
            if word[0] in idx_mp:
                for cells in idx_mp[word[0]]:
                    if dfs(cells[0], cells[1], word, get_empty_visited(m, n)):
                        ans.append(word)
                        break
        
        return ans


