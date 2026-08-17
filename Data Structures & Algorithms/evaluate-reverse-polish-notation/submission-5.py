class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque() 
        operators = {
            "+": lambda x, y: x + y, 
            "-": lambda x, y: x - y, 
            "/": lambda x, y: int(x/y), 
            "*": lambda x, y: x * y}
        
        for token in tokens:
            if token not in operators:
                num = int(token) if not token.startswith("-") else -1*int(token[1:])
                stack.append(num)
            else:
                right, left = stack.pop(), stack.pop()
                stack.append(operators[token](left, right))
        
        return stack[-1]