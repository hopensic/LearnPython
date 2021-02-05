from datetime import datetime
from typing import List

'''
tag: ^1551 ^medium ^math
name: ^(Minimum Operations to Make Array Equal)
'''


class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 1:
            return (n + 1) * (n - 1) // 4
        else:
            return n * n // 4


n = 8

t1 = datetime.now()
s = Solution()
print(s.minOperations(n))
t2 = datetime.now()
print(t2 - t1)
