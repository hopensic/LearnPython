from collections import Counter
from datetime import datetime


class Solution:
    def isHappy(self, n: int) -> bool:
        a = set()
        a.add(n)
        while True:
            sums = sum(int(c) ** 2 for c in str(n))
            if sums == 1:
                return True
            elif sums in a:
                return False
            else:
                n = sums
                a.add(sums)


arr1 = 19

t1 = datetime.now()
s = Solution()
print(s.isHappy(arr1))
t2 = datetime.now()
print(t2 - t1)
