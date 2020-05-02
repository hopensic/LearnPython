from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        replace_idx = 1
        last_num = nums[0]

        for i in range(len(nums)):
            if nums[i] != last_num:
                nums[replace_idx] = nums[i]
                last_num = nums[i]
                replace_idx += 1
        return replace_idx


nums = [0,0,1,1,1,2,2,3,3,4]
solution = Solution()
print(solution.removeDuplicates(nums))
