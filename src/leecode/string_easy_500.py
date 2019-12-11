class Solution:
    def findWords(self, words):
        # a = [sum(map(word.lower().count, row) for word in words) for row in ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']]
        # t = [x for x in [sum(map('Alaska'.lower().count, alph)) for alph in ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']] if len('Alaska') == x]
        # t = [word for _ in [sum(map(word.lower().count, alph)) for alph in ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']] for word in words if len(word) == x]

        # a = [sum(map('dad'.lower().count, alph)) for alph in ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']]

        dic = {word: [sum(map(word.lower().count, alph)) for alph in ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']] for word in
               words}
        t = [word for word, value_list in dic.items() if value_list.count(len(word)) == 1]
        return [word for word in words if t.count(word) == 1]


lst = ["asdfghjkla", "qwertyuiopq", "zxcvbnzzm", "asdfghjkla", "qwertyuiopq", "zxcvbnzzm"]

s = Solution()
print(s.findWords(lst))
