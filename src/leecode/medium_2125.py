from datetime import datetime
from typing import List

'''
tag: ^2125 ^medium ^array ^math ^string ^matrix
name: ^(Number of Laser Beams in a Bank)
'''


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lst = list(filter(lambda x: x > 0, [lt.count('1') for lt in bank]))
        if len(lst) == 1:
            return 0
        return sum([lst[i] * lst[i + 1] for i in range(len(lst) - 1)])


bank = ["011001", "000000", "010100", "001000"]

t1 = datetime.now()
s = Solution()
print(s.numberOfBeams(bank))
t2 = datetime.now()
print(t2 - t1)
