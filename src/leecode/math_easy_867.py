class Solution:
    def transpose(self, A):
        # return [list(t) for t in list(zip(*A))]
        return list(zip(*A))


lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

s = Solution()
print(s.transpose(lst))
