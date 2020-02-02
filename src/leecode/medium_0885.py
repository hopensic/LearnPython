from datetime import datetime

'''
tag: ^0885 ^medium ^math
name: ^(Spiral Matrix III)
'''


class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int):
        res = []
        loop_count = max(r0, R - r0, c0, C - c0) + 2
        destX, destY = c0, r0
        mat = [[0] * C for _ in range(R)]
        total = R * C
        c = 0

        for num in range(1, loop_count):
            # 求 east的方向
            srcX = destX
            srcY = destY
            destX = c0 + num if c0 + num < C else C - 1
            destY = srcY
            for i in range(srcX, destX + 1):
                if mat[srcY][i] == 0:
                    mat[srcY][i] += 1
                    res.append((srcY, i))
                    c += 1
                    if c == total:
                        break
            # 求 south的方向
            srcX = destX
            srcY = destY
            destX = srcX
            destY = r0 + num if r0 + num < R else R - 1
            for i in range(srcY, destY + 1):
                if mat[i][srcX] == 0:
                    mat[i][srcX] += 1
                    res.append((i, srcX))
                    c += 1
                    if c == total:
                        break
            # west
            srcX = destX
            srcY = destY
            destX = c0 - num if c0 - num >= 0 else 0
            destY = srcY
            for i in range(srcX, destX - 1, -1):
                if mat[srcY][i] == 0:
                    mat[srcY][i] += 1
                    res.append((srcY, i))
                    c += 1
                    if c == total:
                        break
            # north
            srcX = destX
            srcY = destY
            destX = srcX
            destY = r0 - num if r0 - num >= 0 else 0
            for i in range(srcY, destY - 1, -1):
                if mat[i][srcX] == 0:
                    mat[i][srcX] += 1
                    res.append((i, srcX))
                    c += 1
                    if c == total:
                        break

        return res


R = 3
C = 3
r0 = 2
c0 = 2

t1 = datetime.now()
s = Solution()
print(s.spiralMatrixIII(R, C, r0, c0))
t2 = datetime.now()
print(t2 - t1)
