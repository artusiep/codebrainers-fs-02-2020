class Dzwi:
    def open(self):
        print(f"Open {self} of id: {id(self)}")


class Butelka:
    def open(self):
        print(f"Open {self} of id: {id(self)}")


class Okno:
    def open(self):
        print(f"Open {self} of id: {id(self)}")


class Plik:
    def open(self):
        print(f"Open {self} of id: {id(self)}")

dzwi = Dzwi()
dzwi2 = Dzwi()
things = [dzwi, Butelka(), Okno(), Plik()]
for thing in things:
    thing.open()

print(id(dzwi))
print(id(dzwi2))
print(dzwi == dzwi2)

