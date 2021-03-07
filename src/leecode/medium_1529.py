from datetime import datetime
from typing import List

'''
tag: ^1529 ^medium ^string
name: ^(Bulb Switcher IV)
'''


class Solution:
    def minFlips(self, target: str) -> int:
        le = len(target)
        res = 0
        pre = '1'
        for idx, ch in enumerate(target):
            if ch == '1':
                break
        else:
            return 0
        res += 1
        for i in range(idx + 1, le):
            if target[i] == pre:
                continue
            else:
                res += 1
                pre = target[i]
        return res


target = "0010101"

t1 = datetime.now()
s = Solution()
print(s.minFlips(target))
t2 = datetime.now()
print(t2 - t1)
