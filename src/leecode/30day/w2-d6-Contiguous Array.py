from datetime import datetime


class Solution:
    def findMaxLength(self, nums: list) -> int:
        if len(nums) < 2:
            return 0
        # 需要返回的值，最长子数组的长度
        maxlen = 0
        # 总体思路 ，将数组内所有的0变成-1，在变成-1的同时计算前缀和
        # -----------------------------
        # 计算前缀和
        # 1.计算前缀和的第一个数
        # 2.计算前缀和的后面所有数
        # ------------------------

        # 1.计算前缀和的第一个数
        prefix_sum = [nums[0] if nums[0] == 1 else -1]

        # 2.计算前缀和的后面所有数
        for i in range(1, len(nums)):
            if nums[i] == 1:
                prefix_sum.append(prefix_sum[i - 1] + 1)
            else:
                prefix_sum.append(prefix_sum[i - 1] - 1)
            # 如果前缀和是0，代表当前的数组是最长的
            if prefix_sum[-1] == 0:
                maxlen = 1 + i

            if i - (maxlen + 2) >= 0:
                if prefix_sum[i] == prefix_sum[i - (maxlen + 2)]:
                    pass
                    # maxlen = i-
        return maxlen


arr = [0, 0, 1, 0, 0, 0, 1, 1]
t1 = datetime.now()
s = Solution()
print(s.findMaxLength(arr))
t2 = datetime.now()
print(t2 - t1)
