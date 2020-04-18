import unittest


class Solution:
    def minPathSum(self, grid: list) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        if m == 1:
            return sum(grid[0])
        if n == 1:
            return sum([grid[i][0] for i in range(m)])

        for col in range(1, n):
            grid[0][col] += grid[0][col - 1]
        for row in range(1, m):
            grid[row][0] += grid[row - 1][0]

        for row in range(1, m):
            for col in range(1, n):
                grid[row][col] += min(grid[row][col - 1], grid[row - 1][col])
        return grid[m - 1][n - 1]


class TestSolution(unittest.TestCase):
    def test_minPathSum(self):
        param3 = [[1], [2]]

        param0 = [[1, 3, 1],
                  [1, 5, 1],
                  [4, 2, 1]]
        param1 = [[1, 3, 1, 2],
                  [2, 1, 2, 3],
                  [1, 3, 1, 4],
                  [2, 1, 1, 2]]
        solution = Solution()
        self.assertEqual(3, solution.minPathSum(param3))
        self.assertEqual(7, solution.minPathSum(param0))
        self.assertEqual(10, solution.minPathSum(param1))


if __name__ == '__main__':
    unittest.main()
