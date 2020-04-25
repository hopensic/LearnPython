import unittest
import bisect
from leecode.common.commons import TreeNode


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
    def __init__(self):
        # self.lst = [
        #     [0, 0, 0, 0, 0, 0, 1],
        #     [0, 0, 0, 0, 1, 1, 1],
        #     [0, 0, 1, 1, 1, 1, 1],
        #     [0, 0, 0, 0, 0, 0, 1]
        # ]

        self.lst =[[0,0],[0,0]]

    def get(self, x: int, y: int) -> int:
        return self.lst[x][y]

    def dimensions(self) -> list:
        return [len(self.lst), len(self.lst[0])]


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        lst = binaryMatrix.dimensions()
        m, n = lst[0], lst[1]

        # 寻找该列的所有行，如果有一个为1，则返回True
        def is_include_one(col: int):
            for i in range(m):
                if binaryMatrix.get(i, col) == 1:
                    return True
            return False

        # not all(binaryMatrix.get(i, 2) ==0  for i in range(m))

        left, right = 0, n - 1
        last_appear_one = n - 1
        while left <= right:
            if left == right:
                if is_include_one(left):
                    return min(left, last_appear_one)
                else:
                    if left == n - 1:
                        return -1
                    else:
                        return last_appear_one
            else:
                middle = int((right + left) / 2)
                if is_include_one(middle):
                    last_appear_one = middle
                    right = middle - 1
                else:
                    left = middle + 1
        return last_appear_one


b = BinaryMatrix()
solution = Solution()
print(solution.leftMostColumnWithOne(b))
