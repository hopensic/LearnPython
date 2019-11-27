class Solution:
    def oddCells(self, n: int, m: int, indices):
        matrix = [[0] * m for _ in range(n)]

        for i in [line[0] for line in indices]:
            for x in range(m):
                matrix[i][x] += 1
        for j in [line[1] for line in indices]:
            for k in range(n):
                matrix[k][j] += 1
        return sum(matrix[i][j] % 2 != 0 for i in range(n) for j in range(m))


lst = [[1, 1], [1, 1]]
s = Solution()
print(s.oddCells(2, 2, lst))
