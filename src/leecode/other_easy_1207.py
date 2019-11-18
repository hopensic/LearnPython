class Solution:
    def uniqueOccurrences(self, arr):
        d = {}
        e = {}
        for x in arr:
            if x in d:
                d[x] = d[x] + 1
            else:
                d[x] = 1
        for value in d.values():
            if value in e:
                return False
            else:
                e[value] = value
        return True


arr = [1, 2, 2, 1, 1, 3]

so = Solution()
print(so.uniqueOccurrences(arr))
