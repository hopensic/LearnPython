class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        maps = {}
        chars1 = 'abcdefghi'
        chars2 = 'jklmnopqrstuvwxyz'

        for i in range(len(chars1)):
            maps[str(i + 1)] = chars1[i]

        for i in range(len(chars2)):
            maps[str(i + 10) + '#'] = chars2[i]

        arr = s.split('#')
        if len(arr[-1]) == 0:
            t = -1
        else:
            t = len(arr) - 1
        for char in arr[0:t]:
            if len(char) > 0:
                if len(char) < 2:
                    res.extend([maps[str(i)] for i in char])
                else:
                    res.extend([maps[str(i)] for i in char[:-2]])
                    res.append(maps[''.join(char[-2:]) + '#'])
        if t != -1:
            res.extend([maps[str(i)] for i in arr[-1]])

        return ''.join(res)


lst = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
# lst = "23"
s = Solution()
print(s.freqAlphabets(lst))
