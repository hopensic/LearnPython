from datetime import datetime
from typing import List

'''
tag: ^1816 ^easy ^string
name: ^(Truncate Sentence)
'''


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        cnt = 0
        for idx, ch in enumerate(s):
            if ch == ' ':
                cnt += 1
                if cnt == k:
                    return s[0:idx]
        else:
            return s


arr1 = "What is the solution to this problem"
k = 2

t1 = datetime.now()
s1 = Solution()
print(s1.truncateSentence(arr1, k))
t2 = datetime.now()
print(t2 - t1)
