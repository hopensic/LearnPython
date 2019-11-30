class Solution:
    def removeDuplicates(self, S: str) -> str:
        t = []
        for char in S:
            if len(t) == 0:
                t.append(char)
                continue
            if char == t[len(t) - 1]:
                t.pop()
            else:
                t.append(char)
        return ''.join(t)


input1 = "cabbaca"

s = Solution()
print(s.removeDuplicates(input1))
