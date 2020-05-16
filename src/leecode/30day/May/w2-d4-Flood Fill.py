from collections import Counter, defaultdict
from datetime import datetime
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        source = image[sr][sc]

        def dfs_fill(row, col):
            if image[row][col] == source:
                image[row][col] = -1
                if row > 0: dfs_fill(row - 1, col)
                if col > 0: dfs_fill(row, col - 1)
                if row < len(image) - 1: dfs_fill(row + 1, col)
                if col < len(image[0]) - 1: dfs_fill(row, col + 1)

        dfs_fill(sr, sc)

        for i in range(len(image)):
            for j in range(len(image[0])):
                image[i][j] = newColor if image[i][j] == -1 else image[i][j]

        return image


image = [[0, 0, 0], [0, 1, 1]]
sr = 1
sc = 1
newColor = 1
t1 = datetime.now()
s1 = Solution()
print(s1.floodFill(image, sr, sc, newColor))
t2 = datetime.now()
print(t2 - t1)
