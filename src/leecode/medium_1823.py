from datetime import datetime
from typing import List

'''
tag: ^1823 ^medium ^array
name: ^(Find the Winner of the Circular Game)
'''


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = [i + 1 for i in range(n)]
        start = 0
        while n > 1:
            jump_step = k % n
            tmp = (start + jump_step) % len(res) - 1
            if tmp < len(res):
                start = tmp
                res.remove(res[start])
                if start < 0:
                    start = 0
            else:
                start = tmp % len(res)
                res.remove(res[start])
            n -= 1

        return res[0]


n = 5
k = 3

t1 = datetime.now()
s = Solution()
print(s.findTheWinner(n, k))
t2 = datetime.now()
print(t2 - t1)
