from datetime import datetime
from leecode.common.common_class import TreeNode

'''
tag: ^1028 ^hard ^dfs
name: ^(Recover a Tree From Preorder Traversal)
'''


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        stack, i = [], 0
        while i < len(S):
            level, val = 0, ""
            while i < len(S) and S[i] == '-':
                level, i = level + 1, i + 1
            while i < len(S) and S[i] != '-':
                val, i = val + S[i], i + 1
            while len(stack) > level:
                stack.pop()
            node = TreeNode(val)
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]


arr1 = "1-2--3--4-5--6--7"
# arr1 = "1-2--3---4-5--6---7"
# arr1 = "1-401--349---90--88"
# arr1 = "10-7--8"

t1 = datetime.now()
s = Solution()
print(s.recoverFromPreorder(arr1))
t2 = datetime.now()
print(t2 - t1)
