from datetime import datetime
from typing import List

'''
tag: ^1486 ^easy ^array ^bit-manipulation
name: ^(XOR Operation in an Array)
'''


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = start
        for i in range(1, n):
            res ^= start + 2 * i
        return res


n = 5
start = 0

t1 = datetime.now()
s = Solution()
print(s.xorOperation(n, start))
t2 = datetime.now()
print(t2 - t1)
