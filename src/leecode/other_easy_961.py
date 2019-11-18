class Solution:
    def repeatedNTimes(self, A):
        d = {}
        for x in A:
            if x in d:
                return x
            else:
                d[x] = x


arr = [5, 1, 5, 2, 5, 3, 5, 4]

so = Solution()
print(so.repeatedNTimes(arr))
