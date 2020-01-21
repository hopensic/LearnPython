from datetime import datetime
from itertools import accumulate
import operator

'''
tag: ^0062 ^medium ^array ^dp
name: ^(Unique Paths)

比如是4*3
1,1,1,1
1,2,3,4
1,3,6,10
1,4,10,20



'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        # accumulate循环的次数
        loop_count = min(m, n)-1

        # 数组内1的个数
        lst = [1] * max(m, n)
        for _ in range(loop_count):
            lst = list(accumulate(lst, operator.add))
        return lst[-1]


m, n = 23, 11

t1 = datetime.now()
s = Solution()
print(s.uniquePaths(m, n))
t2 = datetime.now()
print(t2 - t1)
