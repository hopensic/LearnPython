from collections import defaultdict
from datetime import datetime
from typing import List

'''
tag: ^1399 ^easy ^array
name: ^(Count Largest Group)
'''


class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic = defaultdict(list)
        for i in range(1, n + 1):
            dic[sum([int(k) for k in str(i)])].append(i)
        res_dic = defaultdict(int)
        for v in dic.values():
            res_dic[len(v)] += 1

        return sorted(res_dic.items(),key=lambda d: d[0],reverse=True)[0][1]



n = 13
t1 = datetime.now()
s = Solution()
print(s.countLargestGroup(n))
t2 = datetime.now()
print(t2 - t1)
