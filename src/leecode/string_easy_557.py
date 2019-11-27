class Solution:
    def reverseWords(self, s: str) -> str:
        t = ''.join([x[::-1] + ' ' for x in s.split(' ')])
        print(t.rstrip())


string = "Let's take LeetCode contest"

ss = Solution()
print(ss.reverseWords(string))
