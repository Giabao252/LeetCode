class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min = 0

    def push(self, value: int) -> None:
        if len(self.stack) == 0:
            self.min = value
        elif len(self.stack) > 0 and self.min > value:
            self.min = value
        self.stack.append(value)
        self.min_stack.append(self.min)
        

    def pop(self) -> None:
        self.min = self.min_stack[-2]
        del self.stack[-1]
        del self.min_stack[-1]
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()