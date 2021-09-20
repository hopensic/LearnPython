from datetime import datetime
from typing import List

'''
tag: ^2011 ^easy ^
name: ^(Final Value of Variable After Performing Operations)
'''


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        dic = dict()
        dic["X++"] = 1
        dic["++X"] = 1
        dic["X--"] = -1
        dic["--X"] = -1

        return sum(list(map(lambda x: dic[x], operations)))


arr1 = ["--X", "X++", "X++"]

t1 = datetime.now()
s = Solution()
print(s.finalValueAfterOperations(arr1))
t2 = datetime.now()
print(t2 - t1)
