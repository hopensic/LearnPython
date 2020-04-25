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
            self.value = next(gen, None)
            if self.value:
                self.is_generator = True
                return True
            else:
                self.is_generator = False
                return False

    def next_value(self, gen):
        if self.is_generator:
            self.is_generator = False
            return self.value
        else:
            self.value = next(gen, None)
            return self.value


a = A()
gen = a.test(2)

# a.has_next(gen)
# a.has_next(gen)
# a.has_next(gen)
# print(a.next_value(gen))
# print(a.next_value(gen))
# print(a.next_value(gen))
# print(a.next_value(gen))

while a.has_next(gen):
    print(a.next_value(gen))
