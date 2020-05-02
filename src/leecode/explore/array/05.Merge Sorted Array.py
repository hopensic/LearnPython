class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        end1 = m - 1
        end2 = n - 1
        idx = len(nums1) - 1

        if n == 0:
            return
        if m == 0:
            nums1.clear()
            nums1.extend(nums2)

        while end1 > -1 and end2 > -1:
            if nums1[end1] >= nums2[end2]:
                nums1[idx] = nums1[end1]
                end1 -= 1
            else:
                nums1[idx] = nums2[end2]
                end2 -= 1
            idx -= 1
        if end2 > -1:
            while end2 > -1:
                nums1[idx] = nums2[end2]
                end2 -= 1
                idx -= 1
        print(nums1)


nums1 = [2,0]
m = 1
nums2 = [1]
n = 1
solution = Solution()
print(solution.merge(nums1, m, nums2, n))
