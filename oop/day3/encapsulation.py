class MyClass:
    _protected_class_attribute = "ProtClassAttr"
    class_normal_attribute = "NormalAttribute"

    def normal_method(self):
        self._protected_method()
        print(f"Invoked Normal Method {self._protected_attribute}")

    def _protected_method(self):
        print("Invoked Protected Method")

    def __init__(self):
        self.object_normal_attribute = None
        self._protected_attribute = None


x = MyClass()
print(x.object_normal_attribute)
print(MyClass.class_normal_attribute)

x.normal_method()
# x._protected_method()                      # Violate OOP Encapsulation principle
# print(MyClass._protected_class_attribute)  # Violate OOP Encapsulation principle
# print(x._protected_attribute)              # Violate OOP Encapsulation principle
