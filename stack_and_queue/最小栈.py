from collections import deque

class Stack:
    def __init__(self):
        self.items = deque()
    
    def push(self, val):
        return self.items.append(val)

    def pop(self):
        return self.items.pop()

    def empty(self):
        return len(self.items) == 0

    def top(self):
        return self.items[-1]

class MinStack:
    def __init__(self):
        self.stack = Stack()
        self.mins = Stack()

    def push(self, x: int) -> None:
        if self.stack.empty():
            self.stack.push(x)
            self.mins.push(x)
        else:
            top = self.mins.top()
            if x < top:
                self.mins.push(x)
            else:
                self.mins.push(top)
            self.stack.push(x)

    def pop(self) -> None:
        self.mins.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack.top()


    def getMin(self) -> int:
        return self.mins.top()
