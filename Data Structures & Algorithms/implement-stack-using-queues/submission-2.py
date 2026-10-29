class MyStack:

    def __init__(self):
        self.in_queue = deque()
        self.out_queue = deque()

    def push(self, x: int) -> None:
        self.in_queue.append(x)

    def pop(self) -> int:
        # first transfer the data to the out queue if empty
        if not self.out_queue:
            # r = len(self.queue) - 1
            while self.in_queue:
                self.out_queue.append(self.in_queue.pop())
        # then popleft from outqueue
        if self.out_queue:
            return self.out_queue.popleft()
        return -1
        

    def top(self) -> int:
        if not self.out_queue:
            while self.in_queue:
                self.out_queue.append(self.in_queue.pop())
        if self.out_queue:
            return self.out_queue[0]
        return -1
        

    def empty(self) -> bool:
        if len(self.in_queue) + len(self.out_queue) == 0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()