from collections import deque
from datetime import datetime

'''
tag: ^1381 ^medium ^stack ^design
name: ^(Design a Stack With Increment Operation)
'''


class CustomStack:

    def __init__(self, maxSize: int):
        self.capacity = maxSize
        self.stack = deque()
        self.pointer = 0

    def push(self, x: int) -> None:
        if self.pointer < self.capacity:
            self.stack.appendleft(x)
            self.pointer += 1

    def pop(self) -> int:
        if self.pointer == 0:
            return -1
        self.pointer -= 1
        return self.stack.popleft()

    def increment(self, k: int, val: int) -> None:
        if self.pointer > 0:
            n = self.pointer if k >= self.pointer else k
            for i in range(-1, -1 - n, -1):
                self.stack[i] += val


# s = CustomStack(3)
# s.push(1)
# s.push(2)
# print(s.pop())
# s.push(2)
# s.push(3)
# s.push(4)
# s.increment(5,100)
# s.increment(2,100)
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())

# ------------------------------
# s = CustomStack(28)
# s.push(33)
# s.push(91)
# s.push(76)
# s.push(5)
# s.increment(3, 92)
# s.push(81)
# s.push(11)
# s.pop()
# s.push(85)
# -------------------------------

s = CustomStack(2)
s.push(1)
print(s.pop())
s.increment(8, 100)
print(s.pop())
s.increment(9, 91)
s.push(63)
print(s.pop())
s.push(84)
s.increment(10, 93)
s.increment(6, 45)
s.increment(10, 4)
