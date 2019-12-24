from collections import defaultdict


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        dic = defaultdict(int)
        for x in range(minSize, len(s) + 1):
            tmp_str = s[0:x]
            for j in range(minSize, min(x, maxSize) + 1):
                key = tmp_str[(-1) * j:]
                if len(set(key)) > maxLetters:
                    break
                dic[''.join(key)] += 1

        return max(dic.values()) if len(dic) > 0 else 0


lst = 'aabcaabcenoihaouinteuaabcccdddeeeefffouuiuooeuuuooouuuooouuouo'
maxLetters1 = 20
minSize1 = 2
maxSize1 = 18
s = Solution()
print(s.maxFreq(lst, maxLetters1, minSize1, maxSize1))
