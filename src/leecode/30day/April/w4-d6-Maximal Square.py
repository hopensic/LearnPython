from datetime import datetime


class Solution:

    # 用矩阵右下角的值代表矩阵是否全部含有1
    def maximalSquare(self, matrix: list) -> int:
        square_border = 0

        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        if m == 1:
            return 1 if matrix[0].count("1") > 0 else 0
        if n == 1:
            return 1 if [matrix[i][0] for i in range(m)].count("1") > 0 else 0

        lst = [[0] * n for _ in range(m)]
        for i in range(n):
            lst[0][i] = int(matrix[0][i])
            if square_border == 0:
                square_border = max(square_border, lst[0][i])
        for j in range(m):
            lst[j][0] = int(matrix[j][0])
            square_border = max(square_border, lst[j][0])

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = int(matrix[i][j]) * (
                        min(int(matrix[i - 1][j - 1]), int(matrix[i - 1][j]), int(matrix[i][j - 1])) + 1)
                square_border = max(square_border, matrix[i][j])

        return square_border ** 2


# matrix = [["1", "0", "1", "0", "0"],
#           ["1", "0", "1", "1", "1"],
#           ["1", "1", "1", "1", "1"],
#           ["1", "0", "1", "1", "0"]]

matrix = [["0", "1", ],
          ["1", "0"]]

t1 = datetime.now()
s = Solution()
print(s.maximalSquare(matrix))
t2 = datetime.now()
print(t2 - t1)
