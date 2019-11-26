class Solution:
    def fib(self, N: int) -> int:
        lst = [x for x in range(N + 1)]
        if N == 0: return 0
        if N == 1: return 1
        for x in range(2, N + 1):
            lst[x] = lst[x - 1] + lst[x - 2]
        return lst[N]


s = Solution()
print(s.fib(5))
