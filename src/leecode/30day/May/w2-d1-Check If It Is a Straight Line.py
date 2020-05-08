from collections import Counter
from datetime import datetime
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True

        # x, y = zip(*coordinates)
        # x = set(x)
        # y = set(y)
        #
        # if len(x) == 1 or len(y) == 1:
        #     return True
        y_intercept = coordinates[1][1] - coordinates[0][1]
        x_intercept = coordinates[1][0] - coordinates[0][0]
        k = y_intercept / x_intercept if x_intercept != 0 else float('inf')

        for i in range(2, len(coordinates)):
            y_intercept = coordinates[i][1] - coordinates[i - 1][1]
            x_intercept = coordinates[i][0] - coordinates[i - 1][0]
            temp_k = y_intercept / x_intercept if x_intercept != 0 else float('inf')
            if temp_k != k:
                return False
        return True


coordinates = [[-1, 1], [-6, -4], [-6, 2], [2, 0], [-1, -2], [0, -4]]
t1 = datetime.now()
s1 = Solution()
print(s1.checkStraightLine(coordinates))
t2 = datetime.now()
print(t2 - t1)
