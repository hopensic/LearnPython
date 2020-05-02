import unittest


class Solution:
    def numIslands(self, grid: list) -> int:
        if len(grid)==0:
            return 0



        row_num, col_num = len(grid), len(grid[0])
        def dfs(r, c):
            # 四个方向遍历
            if grid[r][c] == '0' or grid[r][c] == '2':
                return False
            else:
                grid[r][c] = '2'
            if r > 0:
                dfs(r - 1, c)
            if c > 0:
                dfs(r, c - 1)
            if r < row_num - 1:
                dfs(r + 1, c)
            if c < col_num - 1:
                dfs(r, c + 1)

            return True

        n = 0
        for row in range(row_num):
            for col in range(col_num):
                if grid[row][col] == '0' or grid[row][col] == '2':
                    continue
                else:
                    if dfs(row, col):
                        n += 1
        return n


class TestSolution(unittest.TestCase):
    def test_method(self):
        param0 = [["1", "0", "1", "0", "1"],
                  ["0", "1", "1", "0", "1"],
                  ["1", "1", "0", "0", "0"],
                  ["0", "0", "1", "0", "0"]]
        param1=[]
        param2=[["1"]]
        solution = Solution()
        self.assertEqual(4, solution.numIslands(param0))
        self.assertEqual(0, solution.numIslands(param1))
        self.assertEqual(1, solution.numIslands(param2))


if __name__ == '__main__':
    unittest.main()
