class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minVal = val
        elif val < self.minVal:
            self.stack.append(2*val - self.minVal)
            self.minVal = val
        else:
            self.stack.append(val)
        

    def pop(self) -> None:
        top = self.stack.pop()
        
        if top < self.minVal:
            self.minVal = 2*self.minVal - top

    def top(self) -> int:
        top = self.stack[-1]
        if top < self.minVal:
            return self.minVal
        return top

    def getMin(self) -> int:
        return self.minVal


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()