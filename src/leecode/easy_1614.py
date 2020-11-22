from datetime import datetime
from typing import List

'''
tag: ^1614 ^easy ^string
name: ^(Maximum Nesting Depth of the Parentheses)
'''


class Solution:
    def maxDepth(self, s: str) -> int:
        maxnum = 0
        cur = 0
        for ch in s:
            if ch == "(":
                cur += 1
                maxnum = cur if cur > maxnum else maxnum
            elif ch == ")":
                cur -= 1

        return maxnum


s1 = "1+(2*3)/(2-1)"

t1 = datetime.now()
s = Solution()
print(s.maxDepth(s1))
t2 = datetime.now()
print(t2 - t1)
