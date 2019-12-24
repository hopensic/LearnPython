from datetime import datetime

'''
tag: ^766 ^easy ^array
name: ^(Toeplitz Matrix)
'''


class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        R = len(matrix)
        C = len(matrix[0])
        # 计算对角线上半部分
        for c in range(C - 1):
            for i in range((min(R, C - c)) - 1):
                if matrix[i][c + i] != matrix[i + 1][c + i + 1]:
                    return False
                print(matrix[i][c + i])
        # 计算对角线下半部分

        for r in range(1, R - 1):
            for i in range(min(C, R - r) - 1):
                if matrix[r + i][i] != matrix[r + i + 1][i + 1]:
                    return False
                print(matrix[r+i][i])

        return True


matrix1 = [[50, 69, 89, 69],
           [57, 50, 69, 89],
           [0, 57, 50, 69],
           [33, 0, 57, 50],
           [23, 33, 0, 57],
           [26, 23, 33, 0],
           [66, 26, 23, 33],
           [21, 66, 26, 23],
           [18, 21, 66, 0]]

t1 = datetime.now()
s = Solution()
print(s.isToeplitzMatrix(matrix1))
t2 = datetime.now()
print(t2 - t1)
