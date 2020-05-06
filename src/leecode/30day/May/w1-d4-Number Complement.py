from collections import Counter
from datetime import datetime


class Solution:
    def findComplement(self, num: int) -> int:
        return num ^ 2**(len(bin(num))-2)-1


num = 5
t1 = datetime.now()
s = Solution()
print(s.findComplement(num))
t2 = datetime.now()
print(t2 - t1)
