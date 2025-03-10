class MinStack:

    def __init__(self):
        self._data=[]

    def push(self, val: int) -> None:
        self._data.append(val)

    def pop(self) -> None:
        return self._data.pop()

    def top(self) -> int:
        return self._data[-1]
        

    def getMin(self) -> int:
        return min(self._data)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()