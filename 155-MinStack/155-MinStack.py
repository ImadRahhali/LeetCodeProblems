# Last updated: 6/11/2025, 7:03:21 PM
class Node:
    def __init__(self, currentMin, val):
        self.val = val
        self.min = currentMin
class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        if not self.arr:
            currentMin = val
        else:
            currentMin = min(val, self.arr[-1].min)
        self.arr.append(Node(currentMin, val))

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1].val

    def getMin(self) -> int:
        return self.arr[-1].min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()