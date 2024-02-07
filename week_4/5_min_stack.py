# https://leetcode.com/problems/min-stack/

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


def test_min_stack():
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    actual = obj.getMin()
    assert actual == -3, f"getMin failed. Expected -3, but got {actual}"
    obj.pop()
    actual = obj.top()
    assert actual == 0, f"top failed. Expected 0, but got {actual}"
    actual = obj.getMin()
    assert actual == -2, f"getMin failed. Expected -2, but got {actual}"


if __name__ == "__main__":
    test_min_stack()
