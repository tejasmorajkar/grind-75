# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:
    def __init__(self):
        self.main_stack = []
        self.temp_stack = []

    def push(self, x: int) -> None:
        self.main_stack.append(x)

    def pop(self) -> int:
        if not self.main_stack:
            raise ValueError("Queue is empty. Cannot perform pop() operation")
        while len(self.main_stack) > 0:
            self.temp_stack.append(self.main_stack.pop())
        result = self.temp_stack.pop()
        while self.temp_stack:
            self.main_stack.append(self.temp_stack.pop())
        return result


    def peek(self) -> int:
        if not self.main_stack:
            raise ValueError("Queue is empty. Cannot perform peek() operation")
        while len(self.main_stack) > 0:
            ele = self.main_stack.pop()
            self.temp_stack.append(ele)
        result = ele
        while self.temp_stack:
            self.main_stack.append(self.temp_stack.pop())
        return result

    def empty(self) -> bool:
        return len(self.main_stack) == 0


obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
print(param_2)
param_3 = obj.peek()
print(param_3)
param_4 = obj.empty()
print(param_4)