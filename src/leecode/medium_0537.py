from datetime import datetime

'''
tag: ^0537 ^medium ^math ^string
name: ^(Complex Number Multiplication)
'''


class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        arr_a = a.split('+')
        arr_b = b.split('+')
        a1 = int(arr_a[0])
        b1 = int(arr_a[1][:-1])

        c1 = int(arr_b[0])
        d1 = int(arr_b[1][:-1])

        x = a1 * c1 - b1 * d1
        y = a1 * d1 + b1 * c1

        res = str(x) + '+' + str(y) + 'i'

        return res


a = '-1+-1i'
b = '1+1i'

t1 = datetime.now()
s = Solution()
print(s.complexNumberMultiply(a, b))
t2 = datetime.now()
print(t2 - t1)
