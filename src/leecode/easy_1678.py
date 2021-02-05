from datetime import datetime
from typing import List

'''
tag: ^1678 ^easy ^string
name: ^(Goal Parser Interpretation)
'''


class Solution:
    def interpret(self, command: str) -> str:
        res = []
        i = 0
        while i < len(command):
            if command[i] == 'G':
                res.append('G')
                i += 1
            elif command[i] == ')':
                res.append('o')
                i += 1
            elif command[i] == ('a'):
                res.append('a')
                res.append('l')
                i += 3
            else:
                i += 1
        return ''.join(res)


command = "G()()()()(al)"

t1 = datetime.now()
s = Solution()
print(s.interpret(command))
t2 = datetime.now()
print(t2 - t1)
