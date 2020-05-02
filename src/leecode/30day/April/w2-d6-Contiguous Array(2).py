from datetime import datetime


# 已解决

class Solution:
    def findMaxLength(self, nums: list) -> int:
        dic = {}
        maxlen = 0
        prefix_sum = [0]

        for i in range(0, len(nums)):
            # 计算前缀和
            prefix_sum.append(prefix_sum[i] + (1 if nums[i] == 1 else -1))
            # 前缀和的最后一个数
            last_prefix_sum = prefix_sum[-1]
            # 如果前缀和最后一个数为0，那么返回整个数组长度
            if last_prefix_sum == 0:
                maxlen = i+1
                continue
            if last_prefix_sum in dic:
                maxlen = max(maxlen, i - dic[last_prefix_sum])
            else:
                dic[last_prefix_sum] = i

        return maxlen


arr = [0, 0, 1, 0, 0, 0, 1, 1]
# arr = [0,1]
t1 = datetime.now()
s = Solution()
print(s.findMaxLength(arr))
t2 = datetime.now()
print(t2 - t1)
