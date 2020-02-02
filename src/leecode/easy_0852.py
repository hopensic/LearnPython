'''
tag: ^852 ^easy ^binary-search
name: ^(Intersection of Two Linked Lists)
'''


class Solution:
    def peakIndexInMountainArray(self, A):
        for i in range(0, len(A)):
            if i + 1 == len(A):
                return len(A) - 1
            if (A[i + 1] > A[i]):
                continue
            else:
                return i


lst = [0, 1, 2, 1]
s = Solution()
print(s.peakIndexInMountainArray(lst))
