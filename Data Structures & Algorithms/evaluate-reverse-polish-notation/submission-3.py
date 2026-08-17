class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = collections.deque()
        operators = { 
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }

        def evaluate():
            token = stack.pop()
            if token in operators:
                right = evaluate()
                left = evaluate()
                return operators[token](left, right)
            return (-1 * int(token[1:])) if token.startswith("-") else int(token)
        
        for token in tokens:
            stack.append(token)
        
        return evaluate()