from collections import Counter
from datetime import datetime
from typing import List

'''
tag: ^791 ^medium ^string
name: ^(Custom Sort String)
'''


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        s1, s2 = Counter(S), Counter(T)
        res = []
        for k in s1.keys():
            if k in s2:
                res.append(k * s2[k])
                del s2[k]
        for k, v in s2.items():
            res.append(k * v)
        return ''.join(res)


S = "cba"
T = "zabbdact"

t1 = datetime.now()
s = Solution()
print(s.customSortString(S, T))
t2 = datetime.now()
print(t2 - t1)
