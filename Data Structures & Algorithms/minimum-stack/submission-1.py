class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("infinity")
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = min(self.min, val)

    def pop(self) -> None:
        deleted = self.top()
        self.stack.pop()
        if (deleted == self.min):
            if len(self.stack):
                self.min = min(self.stack)
            else:
                self.min = float("infinity")
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
        
