from datetime import datetime
from typing import List

'''
tag: ^1769 ^medium ^array ^greedy
name: ^(Minimum Number of Operations to Move All Balls to Each Box)
'''


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        num_of_one = 0 if boxes[0] == '0' else 1
        for idx, i in enumerate(boxes):
            if idx == 0:
                res.append(0)
                continue
            if i == '1':
                res.append(res[-1] + num_of_one)
                for j in range(idx):
                    res[j] += idx - j
                num_of_one += 1
            if i == '0':
                res.append(res[-1] + num_of_one)
        return res


arr1 = "110"

t1 = datetime.now()
s = Solution()
print(s.minOperations(arr1))
t2 = datetime.now()
print(t2 - t1)
