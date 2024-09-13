import collections


def executeInstructions(n, start, s):
    ns = len(s)
    (x0, y0), (x, y) = start, (0, 0)
    res = range(ns, 0, -1)
    count = collections.defaultdict(set)<
    count[x0, None].add(0)
    count[None, y0].add(0)
    for i in range(ns):
        if s[i] == 'L': y -= 1
        if s[i] == 'R': y += 1
        if s[i] == 'U': x -= 1
        if s[i] == 'D': x += 1
        count[x0 - x, None].add(i + 1)
        count[None, y0 - y].add(i + 1)
        for key in [(n - x, None), (None, n - y), (-x - 1, None), (None, -y - 1)]:
            for j in count[key]:
                if res[j] > i - j:
                    res[j] = i - j
            count[key] = set()
    return res


n = 3
start = (0, 1)
s = "RRDDLU"

executeInstructions(n, start, s);
