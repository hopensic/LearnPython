from datetime import datetime

'''
tag: ^1329 ^medium ^array ^sort
name: ^(Sort the Matrix Diagonally)
'''


class Solution:
    def diagonalSort(self, mat):
        m, n = len(mat), len(mat[0])
        if m == 1 or n == 1:
            return mat
        tmp_list = []
        for j in range(n - 1):
            num = min(m, n - j)
            tmp_list.clear()
            for x in range(num):
                tmp_list.append(mat[x][j + x])
            tmp_list.sort()
            for x in range(num):
                mat[x][j + x] = tmp_list[x]
        for i in range(1, m - 1):
            num = min(n, m - i)
            tmp_list.clear()
            for x in range(num):
                tmp_list.append(mat[i + x][x])
            tmp_list.sort()
            for x in range(num):
                mat[i + x][x] = tmp_list[x]
        return mat


arr1 = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]

t1 = datetime.now()
s = Solution()
print(s.diagonalSort(arr1))
t2 = datetime.now()
print(t2 - t1)
