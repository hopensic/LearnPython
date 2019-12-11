class Solution:
    def numberOfLines(self, widths, S) -> list:
        t = 'abcdefghijklmnopqrstuvwxyz'
        num = 0
        dic = {k: v for k, v in zip(t, widths)}
        total_count = 0
        for ch in S:
            if total_count + dic[ch] > 100:
                num += 1
                total_count = 0
            total_count += dic[ch]

        return [num + 1, total_count]


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
string = 'abcdefghioeuijkfilmnopithourxouintinteuiqrstuvwxyz'

s = Solution()
print(s.numberOfLines(lst, string))
