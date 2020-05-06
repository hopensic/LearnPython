from collections import Counter
from datetime import datetime


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s)==0:
            return -1
        dic = {}
        for idx, ch in enumerate(s):
            if ch in dic:
                dic[ch] = -1
            else:
                dic[ch] = idx
        for k, v in dic.items():
            if v != -1:
                return v
        else:
            return -1


str1 = "aabcb"
t1 = datetime.now()
s1 = Solution()
print(s1.firstUniqChar(str1))
t2 = datetime.now()
print(t2 - t1)
