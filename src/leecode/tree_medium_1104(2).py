class Solution:
    def pathInZigZagTree(self, label: int) -> list:
        if label == 1:
            return [1]
        num_list = []
        k = 1
        n = 0
        while True:
            # 增加第n行
            n += k
            for i in range(n - k + 1, n + 1):
                num_list.append(i)
            if n > label:
                break
            # 增加第n+1行
            k *= 2
            n += k
            for i in list(range(n, n - k, -1)):
                num_list.append(i)
            if n > label:
                break
            #
            k *= 2

        real_pos = num_list.index(label)
        pos_lst = [real_pos]
        while True:
            k = int(real_pos / 2 - 1) if real_pos % 2 == 0 else int(real_pos / 2)
            pos_lst.append(k)
            real_pos = k
            if k == 0:
                break

        return [num_list[i] for i in pos_lst[::-1]]


s = Solution()
print(s.pathInZigZagTree(59345))
