from datetime import datetime
from typing import List

'''
tag: ^1603 ^easy ^design
name: ^(Design Parking System)
'''


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.dic = {}
        self.dic[1] = big
        self.dic[2] = medium
        self.dic[3] = small
        self.current_dic = self.dic.copy()

    def addCar(self, carType: int) -> bool:
        if self.current_dic[carType] == 0:
            return False
        else:
            self.current_dic[carType] = self.current_dic[carType] - 1
            return True


park = ParkingSystem(1, 2, 3)
park.addCar(1)

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
