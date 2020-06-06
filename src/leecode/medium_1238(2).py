from datetime import datetime
from typing import List

'''
tag: ^1238 ^medium ^math
name: ^(Circular Permutation in Binary Representation)
'''


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        lst = []
        for i in range(1 << n):
            lst.append(start ^ i ^ i >> 1)
        return lst


n = 3
start = 2

t1 = datetime.now()
s = Solution()
print(s.circularPermutation(n, start))
t2 = datetime.now()
print(t2 - t1)
