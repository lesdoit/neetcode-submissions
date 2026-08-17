class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = collections.deque()
        
        # add open paran if open_n < n
        # add close param if close_n < open_n 
        # add the current stack to ans if the length of stack is 2*n
        def dfs(open_n, close_n): 
            if open_n == close_n == n:
                ans.append("".join(stack))
                return
            
            if open_n < n:
                stack.append("(")
                dfs(open_n + 1, close_n)
                stack.pop()
            
            if close_n < open_n:
                stack.append(")")
                dfs(open_n, close_n + 1)
                stack.pop()

        dfs(0, 0)
        
        return ans