from datetime import datetime
from typing import List

'''
tag: ^2079 ^medium ^array
name: ^(Watering Plants)
'''


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cur_capacity = capacity
        res = 0
        le = len(plants)
        cur_pos = 0
        while True:
            if cur_pos == le:
                break
            if cur_capacity >= plants[cur_pos]:
                cur_capacity -= plants[cur_pos]
            else:
                res += 2 * cur_pos
                cur_capacity = capacity
                cur_capacity -= plants[cur_pos]
            cur_pos += 1
        return res + le


plants =  [7,7,7,7,7,7,7]
capacity = 8

t1 = datetime.now()
s = Solution()
print(s.wateringPlants(plants, capacity))
t2 = datetime.now()
print(t2 - t1)
