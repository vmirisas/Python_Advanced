class MyIterator:
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        self.n += 10
        if self.n <= 100:
            return list(range(self.n - 10, self.n))
        else:
            raise StopIteration


for stream_data in MyIterator():
    for data in stream_data:
        print(f"{data}{stream_data}")
