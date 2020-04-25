from collections import Counter
from datetime import datetime

'''
tag: ^1394 ^easy ^array
name: ^(Find Lucky Integer in an Array)
'''


class Solution:
    def findLucky(self, arr: list) -> int:
        x = sorted({k: v for k, v in Counter(arr).items() if k == v}, reverse=True)
        return x[0] if len(x) > 0 else -1


arr1 = [11, 2, 2, 2, 6, 6, 6, 6, 7, 10]

t1 = datetime.now()
s = Solution()
print(s.findLucky(arr1))
t2 = datetime.now()
print(t2 - t1)
