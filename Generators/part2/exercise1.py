class MyIterator:
    def __iter__(self):
        self.n = 9
        return self

    def __next__(self):
        self.n += 1
        if self.n < 21:
            return self.n ** 2
        else:
            raise StopIteration


for n in MyIterator():
    print(n)

"""def f():
    yield 10 ** 2
    yield 11 ** 2
    yield 12 ** 2
    yield 13 ** 2
    yield 14 ** 2
    yield 15 ** 2
    yield 16 ** 2
    yield 17 ** 2
    yield 18 ** 2
    yield 19 ** 2
    yield 20 ** 2


it = f()
for i in range(10, 21):
    print(next(it))"""


def MyGenerator():
    for i in range(10, 21):
        yield i * i


for i in MyGenerator():
    print(i)

g = (i ** 2 for i in range(10, 21))
for i in g:
    print(i)
