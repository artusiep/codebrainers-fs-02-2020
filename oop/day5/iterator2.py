class OurRange:
    def __init__(self):
        self.start = 0
        self.stop = 10

    def __iter__(self):
        return OurRange()

    def __next__(self):
        self.start += 1

        if self.start > self.stop:
            raise StopIteration

        return self.start


ourRange = OurRange()

our_range_iter = iter(ourRange)
print(next(ourRange))
print(next(ourRange))
print(next(ourRange))
print(next(ourRange))

for x in ourRange:
    print(x)
