"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        if root.children:
            return 1 + self.get_max_depth(root.children)
        else:
            return 1

    def get_max_depth(self, child_lst):
        if child_lst is None:
            return 0
        num = 0
        for node in child_lst:
            tmp = self.get_max_depth(node.children) + 1
            if tmp > num:
                num = tmp
        return num


r5 = Node(5)
r6 = Node(6)
r3 = Node(3)
r3.children = [r5, r6]
r2 = Node(2)
r4 = Node(4)
r1 = Node(1)
r1.children = [r3, r2, r4]

s = Solution()
print(s.maxDepth(r1))
