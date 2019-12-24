import bisect


class Solution:
    def pathInZigZagTree(self, label: int) -> list:
        if label == 1:
            return 1
        haystack = [2 ** n - 1 for n in range(21)][1:]
        pos = bisect.bisect_left(haystack, label)
        num_list = list(range(1, haystack[pos] + 1))

        max_num = num_list[-1]
        index = 1
        inc = 2
        p = 0
        while True:
            if index > len(num_list) - 1:
                break
            num_list[index:index + inc] = reversed(list(range(index + 1, index + inc + 1)))
            index += (1 << (p + 1)) + (1 << (p + 2))
            p += 2
            inc = inc << 2

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
print(s.pathInZigZagTree(234952))
