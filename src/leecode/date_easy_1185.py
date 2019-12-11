import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        t = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        c = datetime.datetime(year, month, day)
        return t[(c.weekday() + 1) % 7]


s = Solution()
print(s.dayOfTheWeek(15, 8, 1993))
print(s.dayOfTheWeek(31, 8, 2019))
print(s.dayOfTheWeek(2, 12, 2019))
print(s.dayOfTheWeek(3, 12, 2019))
print(s.dayOfTheWeek(4, 12, 2019))
print(s.dayOfTheWeek(5, 12, 2019))
print(s.dayOfTheWeek(6, 12, 2019))
print(s.dayOfTheWeek(7, 12, 2019))
