from collections import defaultdict
from datetime import datetime
from typing import List

'''
tag: ^1817 ^medium ^hash-table
name: ^(Finding the Users Active Minutes)
'''


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        res = [0] * k
        dic = defaultdict(set)
        for id, action in logs:
            dic[id].add(action)
        d = defaultdict(int)
        for v in dic.values():
            d[len(v)] += 1
        for key, v in d.items():
            res[key - 1] = v
        return res


logs = [[1, 1], [2, 2], [2, 3]]
k = 4

t1 = datetime.now()
s = Solution()
print(s.findingUsersActiveMinutes(logs, k))
t2 = datetime.now()
print(t2 - t1)
