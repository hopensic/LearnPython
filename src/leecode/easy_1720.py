from datetime import datetime
from typing import List

'''
tag: ^1720 ^easy ^bit-manipulation
name: ^(Decode XORed Array)
'''


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in encoded:
            res.append(i ^ res[-1])

        return res


encoded = [6, 2, 7, 3]
first = 4

t1 = datetime.now()
s = Solution()
print(s.decode(encoded, first))
t2 = datetime.now()
print(t2 - t1)
