from datetime import datetime
from typing import List

'''
tag: ^1544 ^easy ^array ^stack
name: ^(Make the string great)
'''


class Solution:
    def makeGood(self, s: str) -> str:
        ha = {}
        for idx, i in enumerate(range(65, 91)):
            ha[chr(i)] = chr(97 + idx)
            ha[chr(97 + idx)] = chr(i)
        if len(s) == 1:
            return s
        lst = []
        latest = None

        for ch in s:
            if latest is None:
                lst.append(ch)
                latest = ch
                continue
            if ha[latest] == ch:
                lst.pop()
                if len(lst) == 0:
                    latest = None
                else:
                    latest = lst[-1]
            else:
                lst.append(ch)
                latest = ch

        return ''.join(lst)


# s = 'leEeetcode'
# s = 'AaBb'
# s = 'abBAcC'
# s = 'abBAcCd'
s = 'c'

t1 = datetime.now()
ss = Solution()
print(ss.makeGood(s))
t2 = datetime.now()
print(t2 - t1)
