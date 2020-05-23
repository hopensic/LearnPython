from datetime import datetime
from typing import List

'''
tag: ^1450 ^easy ^array
name: ^(Number of Students Doing Homework at a Given Time)
'''


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return [startTime[i] <= queryTime <= endTime[i] for i in range(len(startTime))].count(True)


startTime = [1, 2, 3]
endTime = [3, 2, 7]
queryTime = 4

t1 = datetime.now()
s = Solution()
print(s.busyStudent(startTime, endTime, queryTime))
t2 = datetime.now()
print(t2 - t1)
