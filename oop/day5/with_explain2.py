# with open('blabla.txt') as f:
#     read_file = f.read()
#     print(read_file)
#
# print(f.read())

class OurOpen:
    def __init__(self, file_path):
        self._file_path = file_path

    def __enter__(self):
        print("I'm enter")
        self.file = open(self._file_path)
        return self.file

    def __exit__(self, _, _1, _2):
        self.file.close()
        print("I'm exit")


with OurOpen("blabla.txt") as f:
    print(f)
    print(f.read())
    print("I'm inside with")
    raise Exception


# x = OurOpen("blabla.txt")
# file = x.__enter__()
# x.__exit__()

# print(f.read())
# f1 = open("blabla.txt")
# f2 = open("blabla.txt")
# print(f1.read())
# print(f2.read())