import datetime
from collections import Counter


class Solution(object):
    def numTilePossibilities(self, tiles):
        return tile_possibilities(Counter(tiles))


dic = {}


def tile_possibilities(counts):
    k = counts.__str__()
    if k in dic:
        return dic[k]

    total = 0
    for key in counts.keys():
        if counts[key] > 0:
            new_counts = dict(counts)
            new_counts[key] -= 1
            total += 1 + tile_possibilities(new_counts)
    dic[k] = total
    return total


starttime = datetime.datetime.now()
r = tile_possibilities(Counter('AAAAABBBBCCCDDE'))
# r = tile_possibilities(Counter('AAABBC'))
endtime = datetime.datetime.now()
print(endtime - starttime)
print(r)
