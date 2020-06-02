from collections import Counter
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda lst: (lst[0] ** 2 + lst[1] ** 2))
        return points[:K]
        # a_list = sorted([((lst[0] ** 2 + lst[1] ** 2), lst) for lst in points], key=lambda item: item[0])
        # print(a_list)


points = [[3, 3], [5, -1], [-2, 4]]
K = 2
prerequisites = []
s1 = Solution()
print(s1.kClosest(points, K))
