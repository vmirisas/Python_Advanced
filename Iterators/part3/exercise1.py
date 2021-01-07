class MyIterator:
    def __iter__(self):
        self.n = -1
        return self

    def __next__(self):
        self.n += 2
        if self.n <= 200:
            return self.n
        else:
            raise StopIteration


print(list(MyIterator()))
print(sum(MyIterator()))
