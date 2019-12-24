class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list:
        ret_lst = []
        num = 0
        for index, ch in enumerate(seq):
            if ch == '(':
                num += 1
                ret_lst.append(num % 2)
            else:
                num -= 1
                ret_lst.append((num + 1) % 2)

        return ret_lst


chars = "((()())())"
s = Solution()
print(s.maxDepthAfterSplit(chars))
