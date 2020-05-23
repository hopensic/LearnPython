from collections import Counter
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res, a_index, b_index = [], 0, 0
        le_A = len(A)
        le_B = len(B)
        if le_A == 0 or le_B == 0:
            return res
        while a_index < le_A and b_index < le_B:
            # A和B有重合
            if A[a_index][0] > B[b_index][1]:
                b_index += 1
            elif B[b_index][0] > A[a_index][1]:
                a_index += 1
            # A和B有重合
            else:
                mn = max(A[a_index][0], B[b_index][0])
                mx = min(A[a_index][1], B[b_index][1])
                res.append([mn, mx])
                if mx >= A[a_index][1]:
                    a_index += 1
                else:
                    b_index += 1
        return res


A = [[6, 16], [17, 25]]
B = [[1, 5], [8, 12], [15, 24], [25, 26]]
s1 = Solution()
print(s1.intervalIntersection(A, B))
