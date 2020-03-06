class Solution:
    def countNegatives(self, grid) -> int:
        num = 0
        for lst in grid:
            for x in lst:
                if x < 0:
                    num += 1
        return num


grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
s = Solution()
print(s.countNegatives(grid))
