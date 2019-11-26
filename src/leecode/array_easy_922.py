class Solution:
    def sortArrayByParityII(self, A):
        odd_lst = []
        even_lst = []
        ret = []
        for x in A:
            if x % 2 == 0:
                even_lst.append(x)
            else:
                odd_lst.append(x)

        for e, o in zip(even_lst, odd_lst):
            ret.append(e)
            ret.append(o)
        return ret


lst = [4, 2, 5, 7]
s = Solution()
print(s.sortArrayByParityII(lst))
