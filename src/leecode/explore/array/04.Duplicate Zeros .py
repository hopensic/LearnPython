class Solution:
    def duplicateZeros(self, arr: list) -> None:
        cur_len = 0
        num_of_zero = 0
        end_position = len(arr) - 1
        for idx, i in enumerate(arr):
            if i == 0:
                num_of_zero += 2
                cur_len += 2
            else:
                cur_len += 1
            if cur_len >= len(arr):
                break
        if num_of_zero > 0:
            if cur_len > len(arr):
                arr[end_position] = 0
                end_position -= 1
                idx -= 1
        while idx > -1:
            if arr[idx] == 0:
                arr[end_position], arr[end_position - 1] = 0, 0
                end_position -= 2
            else:
                arr[end_position] = arr[idx]
                end_position -= 1
            idx -= 1
        print(arr)


arr = [1,2,3]
solution = Solution()
print(solution.duplicateZeros(arr))
