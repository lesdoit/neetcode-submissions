class Solution:
    def isValid(self, s: str) -> bool:
        opp = {")": "(", "]": "[", "}": "{"}
        stack = collections.deque()
        for ch in s:
            if ch in ("[", "(", "{"):
                stack.append(ch)
            else:
                if len(stack) >0 and stack[len(stack) - 1] == opp[ch]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0