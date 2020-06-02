import unittest
from collections import defaultdict
from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def dfs(cur: int, color: int):
            colors[cur] = color
            for i in dic[cur]:
                if colors[i] == color:
                    return False
                if colors[i] == 0 and not dfs(i, -color):
                    return False
            return True

        dic = defaultdict(list)
        for lst in dislikes:
            dic[lst[0]].append(lst[1])
            dic[lst[1]].append(lst[0])

        colors = [0] * (N + 1)
        for k in range(1, N + 1):
            if colors[k] == 0:
                res = dfs(k, 1)
                if not res:
                    return False
        return True


class TestSolution(unittest.TestCase):
    def test_possibleBipartition(self):
        param50, param51 = 5, [[1, 2], [1, 5], [3, 4]]
        param40, param41 = 10, [[4, 7], [4, 8], [5, 6], [1, 6], [3, 7], [2, 5], [5, 8], [1, 2], [4, 9], [6, 10],
                                [8, 10], [3, 6], [2, 10], [9, 10], [3, 9], [2, 3], [1, 9], [4, 6], [5, 7], [3, 8],
                                [1, 8], [1, 7], [2, 4]]
        param30, param31 = 5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]

        param20, param21 = 3, [[1, 2], [1, 3], [2, 3]]
        param10, param11 = 4, [[1, 2], [1, 3], [2, 4]]

        solution = Solution()

        self.assertEqual(True, solution.possibleBipartition(param50, param51))
        self.assertEqual(True, solution.possibleBipartition(param40, param41))
        self.assertEqual(False, solution.possibleBipartition(param30, param31))
        self.assertEqual(False, solution.possibleBipartition(param20, param21))
        self.assertEqual(True, solution.possibleBipartition(param10, param11))


if __name__ == '__main__':
    unittest.main()
