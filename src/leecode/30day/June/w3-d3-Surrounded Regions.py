from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:

    def solve(self, board: List[List[str]]) -> None:
        def dfs(r, c):
            nonlocal is_surrounded
            # 四个方向遍历
            if board[r][c] in ('C', 'N', 'X'):
                return
            if board[r][c] == 'O':
                if (r, c) not in region_set:
                    region_set.add((r, c))
                    if r in (0, row_num - 1) or c in (0, col_num - 1):
                        is_surrounded = False
                else:
                    return
            if r > 0:
                dfs(r - 1, c)
            if c > 0:
                dfs(r, c - 1)
            if r < row_num - 1:
                dfs(r + 1, c)
            if c < col_num - 1:
                dfs(r, c + 1)

        def fill_region(letter: str):
            for r, c in region_set:
                board[r][c] = letter

        def flip_all_region():
            for row in range(row_num):
                for col in range(col_num):
                    if board[row][col] == 'C':
                        board[row][col] = 'X'
                    elif board[row][col] == 'N':
                        board[row][col] = 'O'

        row_num = len(board)
        if row_num < 2:
            return
        col_num = len(board[0])
        if col_num < 2:
            return
        is_surrounded = True
        region_set = set()

        for row in range(row_num):
            for col in range(col_num):
                if board[row][col] == 'O':
                    dfs(row, col)
                    fill_region('C') if is_surrounded else fill_region('N')
                    is_surrounded = True
                    region_set.clear()
        flip_all_region()


regions = [["X", "X", "X", "X"],
           ["X", "O", "O", "X"],
           ["X", "X", "O", "X"],
           ["X", "O", "X", "X"]]
s1 = Solution()
t = s1.solve(regions)
print(t)
