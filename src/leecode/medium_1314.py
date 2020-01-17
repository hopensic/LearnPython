from datetime import datetime

'''
tag: ^1314 ^medium ^dp
name: ^(Matrix Block Sum)
'''


class Solution:
    def matrixBlockSum(self, mat, K):
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if i == 0:
                    if j > 0:
                        mat[i][j] += mat[i][j - 1]
                else:
                    if j == 0:
                        mat[i][j] += mat[i - 1][j]
                    else:
                        mat[i][j] += mat[i][j - 1] + mat[i - 1][j] - mat[i - 1][j - 1]

        mat_new = [[0] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                right = n - 1 if j + K >= n else j + K
                left = 0 if j - K < 0 else j - K
                bottom = m - 1 if i + K >= m else i + K
                top = 0 if i - K < 0 else i - K
                temp1, temp2 = 0, 0
                if top > 0:
                    temp1 += mat[bottom][right] - mat[top - 1][right]
                else:
                    temp1 += mat[bottom][right]

                if left > 0:
                    if top > 0:
                        temp2 += mat[bottom][left - 1] - mat[top - 1][left - 1]
                    else:
                        temp2 += mat[bottom][left - 1]

                mat_new[i][j] = temp1 - temp2

        return mat_new


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
K = 2

t1 = datetime.now()
s = Solution()
print(s.matrixBlockSum(mat, K))
t2 = datetime.now()
print(t2 - t1)

