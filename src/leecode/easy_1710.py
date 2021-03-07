from datetime import datetime
from typing import List

'''
tag: ^1710 ^easy ^greedy ^sort
name: ^(Maximum Units on a Truck)
'''


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: (x[1]), reverse=True)
        amount = 0
        for num, value in boxTypes:
            if num > truckSize:
                if truckSize > 0:
                    amount += truckSize * value
                return amount
            amount += num * value
            truckSize -= num

        return amount


boxTypes = [[1, 3], [2, 2], [3, 1]]
truckSize = 4

t1 = datetime.now()
s = Solution()
print(s.maximumUnits(boxTypes, truckSize))
t2 = datetime.now()
print(t2 - t1)
