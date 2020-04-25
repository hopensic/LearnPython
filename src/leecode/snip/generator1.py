class A:
    def __init__(self):
        self.is_generator = False
        self.value = None

    def test(self, N):

        j = 0
        for i in range(N):
            j += 10
            yield j ** 2

    def has_next(self, gen):
        if self.is_generator:
            return True
        else:
            try:
                self.value = next(gen)
                self.is_generator = True
                return True
            except StopIteration:
                self.value = None
                self.is_generator = False
                return False

    def next_value(self, gen):
        if self.is_generator:
            self.is_generator = False
            return self.value
        else:
            try:
                return next(gen)
            except StopIteration:
                self.value = None
                return None


a = A()
gen = a.test(3)

a.has_next(gen)
a.has_next(gen)
a.has_next(gen)
print(a.next_value(gen))
print(a.next_value(gen))
print(a.next_value(gen))
print(a.next_value(gen))

while a.has_next(gen):
    print(a.next_value(gen))
