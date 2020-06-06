from datetime import datetime
from typing import List

'''
tag: ^1238 ^medium ^math
name: ^(Circular Permutation in Binary Representation)
'''


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res = [start]
        c_lst = [1]
        for i in range(1, n):
            c_lst.append(c_lst[-1] << 1)
        total = c_lst[-1] << 1
        nums_set = set()
        nums_set.add(start)

        while True:
            for c in c_lst:
                t = start ^ c
                if t not in nums_set:
                    nums_set.add(t)
                    res.append(t)
                    start = t
                    break
            if len(res) == total:
                return res


n = 3
start = 2

t1 = datetime.now()
s = Solution()
print(s.circularPermutation(n, start))
t2 = datetime.now()
print(t2 - t1)
