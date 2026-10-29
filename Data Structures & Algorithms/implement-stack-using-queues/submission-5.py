class MyStack:

    def __init__(self):
        self.main = deque()
        self.temp = deque()

    def push(self, x: int) -> None:
        self.temp.append(x)
        while self.main:
            self.temp.append(self.main.popleft())
        self.temp, self.main = self.main, self.temp

    def pop(self) -> int:
        if self.main:
            return self.main.popleft()
        return -1

    def top(self) -> int:
        if self.main:
            return self.main[0]
        return -1

    def empty(self) -> bool:
        return not self.main
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()