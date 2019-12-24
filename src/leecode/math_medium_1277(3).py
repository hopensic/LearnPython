from datetime import datetime

'''
tag: ^1277 ^medium ^array  ^dp
name: ^(Count Square Submatrices with All Ones)
'''
class Solution:
    def countSquares(self, matrix) -> int:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(0, m - 1):
            for j in range(0, n - 1):
                matrix[i + 1][j + 1] *= min(matrix[i][j], matrix[i][j + 1], matrix[i + 1][j]) + 1
        return sum(map(sum, matrix))


lst = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]

t1 = datetime.now()
s = Solution()
print(s.countSquares(lst))
t2 = datetime.now()
print(t2 - t1)
