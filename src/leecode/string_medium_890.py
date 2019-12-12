from collections import defaultdict


class Solution:
    def findAndReplacePattern(self, words, pattern: str) -> list:
        ret_lst = []
        pattern_lst = self.get_list(pattern)
        for chars in words:
            if len(chars) != len(pattern):
                continue
            chars_lst = self.get_list(chars)
            for p, c in zip(pattern_lst, chars_lst):
                if p != c:
                    break
            else:
                ret_lst.append(chars)
        return ret_lst

    def get_list(self, S):
        dic = defaultdict(list)
        for index, char in enumerate(S):
            dic[char].append(index)
        return list(dic.values())


lst = ["abc", "eqqed", "deq", "mee", "aqq", "dkd", "ccc", ]
pat = "abb"
s = Solution()
print(s.findAndReplacePattern(lst, pat))
