class MinStack:

    def __init__(self):
        self.s = collections.deque()
        self.m = collections.deque()

    def push(self, val: int) -> None:
        self.s.append(val)
        val = min(val, self.m[-1] if self.m else val)
        self.m.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.m.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1]
        
