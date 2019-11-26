class Solution:
    def minDeletionSize(self, A: list) -> int:
        le = len(A)
        le2 = len(A[0])
        num = 0
        for i in range(le2):
            for j in range(le - 1):
                if A[j][i] > A[j + 1][i]:
                    num += 1
                    break
        return num


lst = ["zyx","wvu","tsr"]

s = Solution()
print(s.minDeletionSize(lst))
