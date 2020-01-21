class Solution:
    def printVertically(self, s: str) -> list:
        arr = s.split(' ')
        m = max([len(x) for x in arr])
        n = len(arr)
        res = [[] for i in range(m)]
        for word in arr:
            for i, w in enumerate(word):
                res[i].append(w)
            for j in range(i + 1, m):
                res[j].append(' ')

        return [''.join(a).rstrip() for a in res]


chars = "TO BE OR NOT TO BE"

s = Solution()
print(s.printVertically(chars))
