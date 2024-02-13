class MinStack:
    def __init__(self):
        self.stack = []
        self.min = [float("inf")]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min.append(min(self.getMin(), val))

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.min.pop()
            return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
