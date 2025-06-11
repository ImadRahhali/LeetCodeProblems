# Last updated: 6/11/2025, 7:33:00 PM
class MyQueue:

    def __init__(self):
        self.stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        tmp = self.stack[0]
        self.stack.pop(0)
        return tmp

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()