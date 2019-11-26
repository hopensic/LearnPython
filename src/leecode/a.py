import time
from collections import Counter


class Solution(object):
    def numTilePossibilities(self, tiles):
        return tile_possibilities(Counter(tiles))


def tile_possibilities(counts):
    total = 0
    for key in counts.keys():
        if counts[key] > 0:
            new_counts = dict(counts)
            new_counts[key] -= 1
            total += 1 + tile_possibilities(new_counts)
    return total


start = time.clock()
r = tile_possibilities(Counter('AAAABBBCCDE'))
end = time.time()
print( (end - start)/1000000.0)
print(r)
