from datetime import datetime

'''
tag: ^1004 ^medium ^two-pointers ^sliding-window
name: ^(Max Consecutive Ones III)
'''


class Solution:
    def longestOnes(self, A, K) -> int:
        sum_k = -1
        count_k = 0

        # 统计连续1的的和的数组
        interval = []

        i = 0
        while i < len(A):
            temp_sum = 0
            if A[i] == 0:
                i += 1
                continue
            while i < len(A) and A[i] == 1:
                temp_sum += 1
                i += 1
            else:
                interval.append(temp_sum)
                sum_k = max(sum_k, temp_sum)
                while i < len(A) and A[i] == 0:
                    i += 1
        if K == 0:
            return sum_k
        else:
            # 窗口的左边缘和右边缘
            first, last = 0, 0
            # 窗口内的sum
            temp_sum = 0

            last_interval = 0

            # 找到第一个K位置的0
            while count_k < K:
                if last == len(A):
                    return len(A)
                temp_sum += 1
                if A[last] == 0:
                    count_k += 1
                last += 1
            else:
                # 如果窗口右边缘刚好是数组的最后一个
                if last == len(A):
                    return len(A)
                while last < len(A):
                    if A[last] == 1:
                        last_interval += 1
                        last += 1
                    else:
                        temp_sum += last_interval
                        sum_k = max(sum_k, temp_sum)
                        break
                else:
                    return len(A)

            # 开始移动窗口
            while True:
                if last == len(A) - 1:
                    break

                # 先判断窗口右边缘
                # 窗口右边缘是1
                if A[last] == 1:
                    last += 1
                    temp_sum += 1
                # 窗口右边缘是0
                else:
                    last += 1
                    temp_sum += 1
                    if last == len(A) - 1:
                        break
                    while last<len(A):





        return sum_k


A1 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
K1 = 2

t1 = datetime.now()
s = Solution()
print(s.longestOnes(A1, K1))
t2 = datetime.now()
print(t2 - t1)
