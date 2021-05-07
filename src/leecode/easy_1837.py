from datetime import datetime
from typing import List

'''
tag: ^1837 ^easy ^math ^bit-Manipulation
name: ^(Intersection of Two Linked Lists)
'''


class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0
        while n > 0:
            res += n % k
            n //= k

        return res


n = 10
k = 10

t1 = datetime.now()
s = Solution()
print(s.sumBase(n, k))
t2 = datetime.now()
print(t2 - t1)
