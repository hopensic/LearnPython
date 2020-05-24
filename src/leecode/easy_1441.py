from datetime import datetime
from typing import List

'''
tag: ^1441 ^easy ^stack
name: ^(Build an Array With Stack Operations)
'''


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        PUSH, POP = "Push", "Pop"
        target_index, range_index = 0, 1

        while target_index < len(target):
            res.append(PUSH)
            if range_index != target[target_index]:
                res.append(POP)
            else:
                target_index += 1
            range_index += 1
        return res


target = [2, 3,4]
n = 4
t1 = datetime.now()
s = Solution()
print(s.buildArray(target, n))
t2 = datetime.now()
print(t2 - t1)
