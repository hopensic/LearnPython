def balancedStringSplit(str):
    cnt = 0
    res = 0
    for c in str:
        if c == 'R':
            cnt += 1
        if c == 'L':
            cnt -= 1
        if (cnt == 0):
            res += 1
    return res


str = "RRLRRLRLLLRL"

a = balancedStringSplit(str)
print(a)
