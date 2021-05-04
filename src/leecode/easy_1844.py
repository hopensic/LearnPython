from datetime import datetime
from typing import List

'''
tag: ^1844 ^easy ^string
name: ^(Replace All Digits with Characters)
'''


class Solution:
    def replaceDigits(self, s: str) -> str:
        res = []
        le = len(s)
        string_array = s[0:le:2]
        num_array = s[1:le:2]

        for idx, ch in enumerate(num_array):
            res.append(string_array[idx])
            res.append(chr(ord(res[-1]) + int(ch)))

        if len(string_array) > len(num_array):
            res.append(string_array[-1])
        return ''.join(res)


arr1 = "a1b2c3d4e"

t1 = datetime.now()
s1 = Solution()
print(s1.replaceDigits(arr1))
t2 = datetime.now()
print(t2 - t1)
