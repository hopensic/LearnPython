from datetime import datetime
from typing import List

'''
tag: ^160 ^easy ^linkedlist
name: ^(Intersection of Two Linked Lists)
'''


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dic = {lst[0]: lst[1] for lst in paths}
        tmp = paths[0][1]
        while tmp in dic:
            tmp = dic[tmp]
        return tmp


paths = [["London", "New York"],
         ["New York", "Lima"],
         ["Lima", "Sao Paulo"]]

t1 = datetime.now()
s = Solution()
print(s.destCity(paths))
t2 = datetime.now()
print(t2 - t1)
