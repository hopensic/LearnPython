class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        bin_a = bin(a)[2:]
        bin_b = bin(b)[2:]
        bin_c = bin(c)[2:]
        len_c = max(len(bin_a), len(bin_b), len(bin_c))
        bin_a = bin_a.zfill(len_c)
        bin_b = bin_b.zfill(len_c)
        bin_c = bin_c.zfill(len_c)
        res = 0

        for i in range(len_c):
            if bin_c[i] == '0':
                if bin_a[i] == '1' and bin_b[i] == '1':
                    res += 2
                elif bin_a[i] == '1' and bin_b[i] == '0':
                    res += 1
                elif bin_a[i] == '0' and bin_b[i] == '1':
                    res += 1


            else:
                if bin_a[i] == '0' and bin_b[i] == '0':
                    res += 1

        return res


a = 8
b = 3
c = 5

s = Solution()
print(s.minFlips(a, b, c))
