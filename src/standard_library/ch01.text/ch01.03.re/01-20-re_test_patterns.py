import re
from typing import List


def test_patterns(text, patterns: List):
    for pattern, desc in patterns:
        print("'{}' ({})\n".format(pattern, desc))
        print("  '{}' ".format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')
            prefix = '.' * (s + n_backslashes)
            print("  {}'{}'".format(prefix, substr))
    return


text1 = 'abbaaabbbbaaaaa'
pattern1 = 'ab'
desc1 = "'a' followed by 'b'"

if __name__ == '__main__':
    test_patterns(text1, [(pattern1, desc1), ])
