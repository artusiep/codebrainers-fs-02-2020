# class BaseClass:
#     pass
#
# class DerivedClass(BaseClass):
#     pass

class Base:
    def __init__(self):
        self.name = "Base"
        print("I'm base class")

    def fun(self):
        print(f"Base class fun {self.name}")


b_blabla = Base()
b_blabla.fun()

print("------------------------")


class Derived1(Base):
    def __init__(self):
        super().__init__()  # Constructor Invocation of base class
        self.name = "Derived"
        print("I'm derived class One")

    def not_so_funny(self):
        print("Name dupa is not funny")


class Derived2(Base):
    def __init__(self):
        super().__init__()
        print("I'm derived class Two")

    def fun(self):
        print("Overridden method")


# b_blabla.not_so_funny() # Not working


dupa = Derived1()
dupa.fun()
dupa.not_so_funny()
print(dupa.name)

derived2 = Derived2()
derived2.fun()
dupa.fun()
