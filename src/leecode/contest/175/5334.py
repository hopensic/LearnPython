from collections import defaultdict
from collections import Counter
import bisect


class TweetCounts:

    def __init__(self):
        self.dic = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.dic[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> list:

        if freq == 'minute':
            lst = self.dic[tweetName]
            left = bisect.bisect_left(lst, startTime)
            right = bisect.bisect(lst, endTime)
            target_lst = lst[left:right]
            ll = [int(target / 60) for target in target_lst]
            c = Counter(ll)
            res = [v for v in c.values()]
            return res
        elif freq == 'hour':
            lst = self.dic[tweetName]
            left = bisect.bisect_left(lst, startTime)
            right = bisect.bisect(lst, endTime)
            target_lst = lst[left:right]
            ll = [int(target / 3600) for target in target_lst]
            c = Counter(ll)
            res = [v for v in c.values()]
            return res
        else:
            lst = self.dic[tweetName]
            left = bisect.bisect_left(lst, startTime)
            right = bisect.bisect(lst, endTime)
            target_lst = lst[left:right]
            ll = [int(target / 86400) for target in target_lst]
            c = Counter(ll)
            res = [v for v in c.values()]
            return res

    def check(self):
        print(self.dic)


t = TweetCounts()
t.recordTweet('aa', 0)
t.recordTweet('aa', 10)
t.recordTweet('aa', 60)
print(t.getTweetCountsPerFrequency("minute", "aa", 20, 59))
#print(t.getTweetCountsPerFrequency("minute", "aa", 0, 60))
# t.recordTweet("aa", 120);
# print(t.getTweetCountsPerFrequency('hour', 'aa', 0, 210))


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
