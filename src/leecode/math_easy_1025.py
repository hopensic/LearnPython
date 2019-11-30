from math import sqrt


class Solution:
    def divisorGame(self, N: int) -> bool:
        Solution.lst = [0] * N
        for i in range(1, N + 1):
            Solution.lst[i - 1] = self.f(i)
        return Solution.lst[N - 1] == 1

    def f(self, n):
        if n == 1:
            Solution.lst[n - 1] = 0
            return 0
        elif n == 2:
            Solution.lst[n - 1] = 1
            return 1
        else:
            # 计算能被n整除的数列表
            divided_list = set()
            divided_list.add(1)
            num = int(sqrt(n))
            for i in range(2, num + 1):
                x = n % i
                if x == 0:
                    divided_list.add(i)
                    divided_list.add(int(n / i))
            for y in divided_list:
                if Solution.lst[n - y - 1] == 0:
                    Solution.lst[n - 1] = 1
                    return 1
            return 0


t = 125
s = Solution()

print('{}:{}'.format(t, s.divisorGame(t)))

print('------------------')
for i in range(1, t + 1):
    print('{}:{}'.format(i, s.divisorGame(i)))
