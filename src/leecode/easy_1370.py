from datetime import datetime
from collections import Counter

'''
tag: ^1370 ^easy ^string ^sort
name: ^(Increasing Decreasing String)
'''


class Solution:
    def sortString(self, s: str) -> str:
        res = []
        tmp = set()
        c = Counter(s)
        lst = list(sorted(Counter(s)))
        while len(c) > 0:
            for ch in lst:
                if c[ch] > 0:
                    res.append(ch)
                    c[ch] -= 1
                    if c[ch] == 0:
                        tmp.add(ch)
            for k in tmp:
                del c[k]
            tmp.clear()

            for ch in lst[::-1]:
                if c[ch] > 0:
                    res.append(ch)
                    c[ch] -= 1
                    if c[ch] == 0:
                        tmp.add(ch)
            for k in tmp:
                del c[k]
            tmp.clear()
        return ''.join(res)


arr1 = "spo"

t1 = datetime.now()
s = Solution()
print(s.sortString(arr1))
t2 = datetime.now()
print(t2 - t1)
