class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        # dic = {(x, y): abs(x - r0) + abs(y - c0) for x in range(R) for y in range(C)}

        return sorted([(x, y) for x in range(R) for y in range(C)], key=lambda p: abs(p[0] - r0) + abs(p[1] - c0))

        # return [list(t[0]) for t in sorted(dic.items(), key=operator.itemgetter(1))]


row = 2
column = 3

r0 = 1
c0 = 2

dic = {(1, 2): 1}

s = Solution()
print(s.allCellsDistOrder(row, column, r0, c0))
