class Ciag:
    def __init__(self, limit):
        self.a = 5
        self.b = 1
        self.limit = limit

    def __next__(self):
        # 1 Sposób
        # temp = self.b
        # self.b = self.b + self.a
        # self.a = temp
        # 2 Sposób
        self.a, self.b = self.b, self.a + self.b

        if self.a >= self.limit:
            raise StopIteration

        return self.a

    def __iter__(self):
        return Ciag(self.limit)


ciag = Ciag(100)

for x in ciag:
    print(x)

