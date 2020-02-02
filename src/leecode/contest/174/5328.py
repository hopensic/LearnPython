class Solution:
    def kWeakestRows(self, mat, k: int) -> list:
        c = [lst.count(1) for lst in mat]
        llst = []
        for idx, x in enumerate(c):
            llst.append((x, idx))
        rlist = sorted(llst, key=lambda item: (item[0], item[1]))
        res = []

        for i in range(k):
            res.append(rlist[i][1])

        return res


mat = [[1, 0, 0, 0],
       [1, 1, 1, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 0]]
k = 2

s = Solution()
print(s.kWeakestRows(mat, k))
