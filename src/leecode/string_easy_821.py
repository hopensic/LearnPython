class Solution:
    def shortestToChar(self, S: str, C: str) -> list:
        le = len(S)
        idx = -1
        position = []
        while (True):
            idx = S.find(C, idx + 1)
            position.append(idx)
            if idx == -1:
                break
        position.pop()
        print(position)
        ret_lst = list(S)

        # 处理第一个找到之前的
        if position[0] > 0:
            ret_lst[0:position[0]] = list(range(1, position[0] + 1))[::-1]
        # 处理中间的
        for i in range(len(position) - 1):
            if position[i + 1] - position[i] > 1:
                ret_lst[position[i] + 1:position[i + 1]] = self.f(position[i + 1] - position[i])

        # 处理最后一个之后的
        if position[-1] < len(S) - 1:
            ret_lst[position[-1]:] = list(range(le - position[-1]))
        for i in position:
            ret_lst[i] = 0

        return ret_lst

    def f(self, n):
        n -= 1
        if n == 1:
            return [1]
        elif n == 2:
            return [1, 1]
        else:
            t = int((n + 1) / 2)
            if (n + 1) % 2 == 0:
                return list(range(1, t + 1)) + (list(range(1, t))[::-1])
            else:
                return list(range(1, t + 1)) + (list(range(1, t + 1)[::-1]))


chars = "uuntitiurcpithountitontuintoepihteucitjkeo"
char = 't'

s = Solution()
print(s.shortestToChar(chars, char))
