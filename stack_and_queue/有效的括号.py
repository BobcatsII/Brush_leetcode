# 详细写法
from collection import deque
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


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        stack = Stack()
        for char in s:
            if stack.empty():
                stack.push(char)
            else:
                top = stack.top()
                if is_pair(char) == top:
                    stack.pop()
                else:
                    stack.push(char)
        return stack.empty()

def is_pair(char):
    if char == ")":
        return "("
    elif char == "]":
        return "["
    elif char == "}":
        return "{"




# 简单写法
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")":"(", "]":"[","}":"{"}
        stack = []
        for i in s:
            if stack and i in dic:
                if stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack

