from datetime import datetime
from typing import List

'''
tag: ^1812 ^easy ^string
name: ^(Determine Color of a Chessboard Square)
'''


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return False if ord(coordinates[0]) % 2 == int(coordinates[1]) % 2 else True


coordinates = "c7"

t1 = datetime.now()
s = Solution()
print(s.squareIsWhite(coordinates))
t2 = datetime.now()
print(t2 - t1)
