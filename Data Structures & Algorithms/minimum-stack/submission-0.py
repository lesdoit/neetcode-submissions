class MinStack:

    def __init__(self):
        self.s = collections.deque()
        self.m = collections.deque()

    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.m) > 0:
            if self.top_m() > val:
                self.m.append(val)
            else:
                self.m.append(self.top_m())
        else:
            self.m.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.m.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1]
    
    def top_m(self):
        return self.m[-1]
        
