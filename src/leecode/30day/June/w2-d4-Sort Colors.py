from random import randint
from typing import List
from bisect import bisect_left, bisect, insort
from itertools import accumulate
import operator


class Solution:

    def sortColors(self, nums: List[int]) -> None:
        # two pointer solution
        le = len(nums)
        zero_pos = 0
        two_pos = le - 1

        while True:
            # search from left to right , to find the one not equal to 0
            while zero_pos < le:
                if nums[zero_pos] == 0:
                    zero_pos += 1
                else:
                    break
            else:
                return
            if zero_pos > two_pos:
                return
            # search from right to left , to find the one not equal to 2
            while two_pos > -1:
                if nums[two_pos] == 2:
                    two_pos -= 1
                else:
                    break
            else:
                return

            if zero_pos > two_pos:
                return

            if nums[zero_pos] == 2 and nums[zero_pos] != nums[two_pos]:
                nums[zero_pos], nums[two_pos] = nums[two_pos], nums[zero_pos]
                two_pos -= 1
                continue
            if nums[two_pos] == 0 and nums[two_pos] != nums[zero_pos]:
                nums[zero_pos], nums[two_pos] = nums[two_pos], nums[zero_pos]
                zero_pos += 1
                continue
            # search from left to right, to find the one equal to 2
            zero_loop = zero_pos
            two_loop = two_pos
            while zero_loop <= two_loop:
                if nums[zero_loop] == 0:
                    nums[zero_loop], nums[zero_pos] = nums[zero_pos], nums[zero_loop]
                    zero_pos += 1
                    break
                elif nums[zero_loop] == 2:
                    nums[zero_loop], nums[two_pos] = nums[two_pos], nums[zero_loop]
                    two_pos -= 1
                    break
                else:
                    zero_loop += 1
            else:
                print(nums)
                return


# nums = [2, 0, 2, 1, 1, 0]
nums = [0, 2]
# nums = [2, 0, 1, 2, 0, 1, 2, 0]
s1 = Solution()
print(s1.sortColors(nums))
