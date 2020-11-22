from datetime import datetime
from typing import List

'''
tag: ^1476 ^medium ^array
name: ^(Subrectangle Queries)
'''


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = [l for l in rectangle]
        self.m = len(self.rectangle)
        self.n = len(self.rectangle[0])

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:

        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.rectangle[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        if 0 <= row < self.m and 0 <= col < self.n:
            return self.rectangle[row]
        else:
            return None


lst = [[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]
s = SubrectangleQueries(lst)
print(s.getValue(0, 2))
s.updateSubrectangle(0, 0, 3, 2, 5)
print(s.getValue(0, 2))
