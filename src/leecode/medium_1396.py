from collections import defaultdict
from datetime import datetime
from typing import List

'''
tag: ^1396 ^medium ^design
name: ^(Design Underground System)
'''


class UndergroundSystem:

    def __init__(self):
        self.count_map = defaultdict(int)
        self.total_time_map = defaultdict(int)
        self.id_map = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id_map[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        k = self.id_map[id][0] + '-' + stationName
        pre_time = self.id_map[id][1]
        self.count_map[k] += 1
        self.total_time_map[k] += t - pre_time
        del self.id_map[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        k = startStation + '-' + endStation
        return self.total_time_map[k] / self.count_map[k]
