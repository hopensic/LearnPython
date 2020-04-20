from datetime import datetime
from collections import defaultdict

'''
tag: ^1356 ^easy ^sort ^bit-manipulation
name: ^(Sort Integers by The Number of 1 Bits)
'''


class Solution:
    def sortByBits(self, arr: list) -> list:
        dic = defaultdict(list)
        res = []
        for i in arr:
            dic[bin(i).count("1")].append(i)
        for k, v in sorted(dic.items()):
            v.sort()
            res.extend(v)
        return res


arr1 = [10, 100, 1000, 10000]

t1 = datetime.now()
s = Solution()
print(s.sortByBits(arr1))
t2 = datetime.now()
print(t2 - t1)
