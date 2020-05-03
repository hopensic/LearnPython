from datetime import datetime
from typing import List

'''
tag: ^1433 ^medium ^string ^greedy
name: ^(Check If a String Can Break Another String)
'''


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        sorted_s1 = ''.join(sorted(s1))
        sorted_s2 = ''.join(sorted(s2))
        mx, mn = 0, 0

        for i in range(len(s1)):
            if sorted_s1[i] < sorted_s2[i]:
                mn += 1
            elif sorted_s1[i] > sorted_s2[i]:
                mx += 1
            else:
                mn += 1
                mx += 1
        return mn == len(s1) or mx == len(s1)


s1 = "yopumzgd"
s2 = "pamntyya"

t1 = datetime.now()
s = Solution()
print(s.checkIfCanBreak(s1, s2))
t2 = datetime.now()
print(t2 - t1)
