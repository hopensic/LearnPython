from datetime import datetime
from typing import List

'''
tag: ^1528 ^easy ^sort
name: ^(Shuffle String)
'''


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = ['_'] * len(s)
        for idx, indice in enumerate(indices):
            d[indice] = s[idx]

        return ''.join(d)


s1 = "codeleet"
indices1 = [4, 5, 6, 7, 0, 2, 1, 3]

t1 = datetime.now()
s = Solution()
print(s.restoreString(s1, indices1))
t2 = datetime.now()
print(t2 - t1)
