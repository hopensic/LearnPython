from collections import deque
from bisect import insort, bisect_left


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.que = deque()
        self.min = 0
        self.minlist = []

    def push(self, x: int) -> None:
        self.que.appendleft(x)
        insort(self.minlist, x)
        self.min = min(self.min, x)

    def pop(self) -> None:
        if len(self.que) > 0:
            x = self.que.popleft()
            pos = bisect_left(self.minlist, x)
            del self.minlist[pos]

    def top(self) -> int:
        if len(self.que) > 0:
            return self.que[0]
        else:
            return -1

    def getMin(self) -> int:
        if len(self.minlist) > 0:
            return self.minlist[0]
        else:
            return None


minstack = MinStack()
minstack.push(2)
minstack.push(4)
minstack.push(1)
minstack.push(3)
minstack.pop()
minstack.pop()
minstack.pop()
minstack.pop()
minstack.pop()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
