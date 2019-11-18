class Solution:
    def flipAndInvertImage(self, A):
        ret_lst = []
        for lst in A:
            ret_lst.append([x^1 for x in lst[::-1]])
        return ret_lst


arr = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]

so = Solution()
print(so.flipAndInvertImage(arr))
