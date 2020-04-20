from datetime import datetime

'''
tag: ^1380 ^easy ^array
name: ^(Lucky Numbers in a Matrix)
'''


class Solution:
    def luckyNumbers(self, matrix: list) -> list:
        minlst = [min(lst) for lst in matrix]
        maxlst = [max(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0]))]
        res = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == minlst[r] == maxlst[c]:
                    res.append(matrix[r][c])

        return res


matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]

t1 = datetime.now()
s = Solution()
print(s.luckyNumbers(matrix))
t2 = datetime.now()
print(t2 - t1)
