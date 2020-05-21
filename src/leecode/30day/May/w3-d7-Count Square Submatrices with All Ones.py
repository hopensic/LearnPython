from collections import Counter
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        if m == 1:
            return matrix[0].count(1)
        if n == 1:
            return [matrix[i][0] for i in m].count(1)

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] *= 1 + min(matrix[i][j - 1], matrix[i - 1][j - 1], matrix[i - 1][j])

        return sum([sum(matrix[i]) for i in range(m)])


matrix = [
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 0]
]

s1 = Solution()
print(s1.countSquares(matrix))
