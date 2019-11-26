from bisect import bisect_left


class RecentCounter:
    lst = []

    def __init__(self):
        RecentCounter.lst.clear()
        RecentCounter.is_init = False

    def ping(self, t: int) -> int:
        RecentCounter.lst.append(t)

        if not RecentCounter.is_init:
            RecentCounter.is_init = True
            return 1

        front = t - 3000
        idx = bisect_left(RecentCounter.lst, front)
        if front < 0:
            return len(RecentCounter.lst)
        return len(RecentCounter.lst[idx:])


obj = RecentCounter()
print(obj.ping(642))
print(obj.ping(1849))
print(obj.ping(3643))
print(obj.ping(5936))
print(obj.ping(6643))
