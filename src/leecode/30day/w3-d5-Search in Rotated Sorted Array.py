import unittest
import bisect


class Solution:
    def search(self, nums: list, target: int) -> int:
        def find_target(t_lst: list, t: int):
            i = bisect.bisect_left(t_lst, t)
            if i == len(t_lst):
                return -1
            return i if t == t_lst[i] else -1

        idx = 0
        target_lst = nums
        le = len(nums)
        if le == 0:
            return -1
        if le == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        while True:
            if len(target_lst) == 0:
                return -1
            elif len(target_lst) == 1:
                if target_lst[0] == target:
                    return idx
                else:
                    return -1

            middle = int(len(target_lst) / 2)
            if target_lst[middle] == target:
                return idx + middle

            left_lst = target_lst[0:middle]
            right_lst = target_lst[middle:]

            # 判断左数组是否正常
            if len(left_lst) == 0:
                target_lst = right_lst
                continue
            elif len(left_lst) == 1:
                if left_lst[0] == target:
                    return idx
                else:
                    idx += 1
                    target_lst = right_lst
                    continue
            # 判断左数组是否正常
            else:
                # 左数组正常
                if left_lst[0] < left_lst[-1]:

                    if left_lst[0] <= target <= left_lst[-1]:
                        tmp_idx = find_target(left_lst,target)
                        if tmp_idx == -1:
                            target_lst = right_lst
                            idx += len(left_lst)
                        else:
                            return idx + tmp_idx
                        continue
                    else:
                        target_lst = right_lst
                        idx += len(left_lst)
                        continue
                # 左数组不正常
                else:
                    if len(right_lst) == 0:
                        target_lst = left_lst
                        continue
                    elif len(right_lst) == 1:
                        if right_lst[0] == target:
                            return idx + 1
                        else:
                            target_lst = left_lst
                            continue
                    else:
                        if right_lst[0] <= target <= right_lst[-1]:
                            tmp_idx = find_target(right_lst, target)
                            if tmp_idx == -1:
                                target_lst = left_lst
                                continue
                            else:
                                return idx + len(left_lst) + tmp_idx
                        else:
                            target_lst = left_lst
                            continue


class TestSolution(unittest.TestCase):
    def test_search(self):
        param60, param61 = [4, 5, 6, 7, 0, 1, 2], 4
        param50, param51 = [4, 5, 6, 7, 0, 1, 2], 2
        param40, param41 = [1, 3, 5], 5
        param30, param31 = [4, 5, 6, 7, 0, 1, 2], 0
        param20, param21 = [4, 5, 6, 7, 0, 1, 2], 3
        param10, param11 = [8, 9, 10, 11, 12, 13, 14, 15, 16, 2, 3, 4, 5, 6, 7], 3

        solution = Solution()
        self.assertEqual(0, solution.search(param60, param61))
        self.assertEqual(2, solution.search(param40, param41))
        self.assertEqual(4, solution.search(param30, param31))
        self.assertEqual(-1, solution.search(param20, param21))
        self.assertEqual(10, solution.search(param10, param11))


if __name__ == '__main__':
    unittest.main()
