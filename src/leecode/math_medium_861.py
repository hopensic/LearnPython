class Solution:
    def matrixScore(self, A) -> int:
        n = len(A[0])
        # 如果只有1列
        # if there is only 1 column
        if n == 1:
            return len(A)

        # 如果只有一行
        # if there in only 1 row
        if len(A) == 1:
            return 2 ** len(A[0]) - 1

        for row in A:
            # 先把第一列所有的0换成1: 需要将第列为0的列进行行转换
            # first transfer all '0' in column 1 to '1'，
            # so it need change the row in which the first column equal to 0
            if row[0] == 0:
                for index, num in enumerate(row):
                    row[index] ^= 1

        # 寻找除第1列外的，0和1的个数，将较大的值放入字典中
        # find count of '0' and '1' in all columns except column 1,
        # and put the bigger count in the dic

        dic = {}
        for i in range(1, n):
            s0 = 0
            s1 = 0
            for row in A:
                if row[i] == 1:
                    s1 += 1
                else:
                    s0 += 1
            dic[n - i - 1] = max(s0, s1)

        return sum((1 << k) * v for k, v in dic.items()) + len(A) * (1 << (n - 1))


lst = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]

s = Solution()
print(s.matrixScore(lst))
