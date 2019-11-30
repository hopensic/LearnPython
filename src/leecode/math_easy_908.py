import random


class Solution:
    def smallestRangeI(self, A, K):
        A.sort()
        b = A[len(A) - 1] - A[0] - 2 * K
        return b if b > 0 else 0


lst = [random.randint(1, 1000) for _ in range(100)]
lst.sort()
n = random.randint(10, 100)
print(lst)
print(n)

s = Solution()
print(s.smallestRangeI(lst, n))
