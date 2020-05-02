class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        if len(nums) == 0:
            return 0
        maxlen = 0
        is_begin = False
        le = 0
        for n in nums:
            if not is_begin:
                if n == 0:
                    continue
                else:
                    is_begin = True
                    le += 1
            else:
                if n == 0:
                    maxlen = max(maxlen, le)
                    is_begin = False
                    le = 0
                else:
                    le += 1

        return max(maxlen, le)


arr = [1, 1, 0, 1, 1, 1]
solution = Solution()
print(solution.findMaxConsecutiveOnes(arr))
