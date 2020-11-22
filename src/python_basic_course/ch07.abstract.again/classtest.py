class Filter:

    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):

    def init(self):
        self.blocked = ['SPAM']


f = Filter()
f.init()
d = f.filter([1, 2, 3])
print(d)

s = SPAMFilter()
s.init()
d = s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'egg', 'SPAM', 'SPAM', 'bacon'])
print(d)

print(SPAMFilter.__base__)