from collections import deque
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> list:
        if not root:
            return []
        stack = []
        lst = []
        stack.append(root)
        while True:
            if len(stack) == 0:
                break
            poped = stack.pop()
            lst.append(poped.val)
            if poped.children:
                stack.extend(poped.children)
        return lst[::-1]


    def preorderWithDeque(self, root: 'Node') -> list:
        if not root:
            return []
        stack = deque()
        lst = []
        stack.append(root)
        while True:
            if len(stack) == 0:
                break
            poped = stack.pop()
            lst.append(poped.val)
            if poped.children:
                stack.extend(poped.children)
        return lst[::-1]


r5 = Node(5)
r6 = Node(6)
r3 = Node(3)
r3.children = [r5, r6]
r2 = Node(2)
r4 = Node(4)
r1 = Node(1)
r1.children = [r3, r2, r4]

s = Solution()
print(s.preorderWithDeque(r1))
