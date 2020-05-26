# with open('blabla.txt') as f:
#     read_file = f.read()
#     print(read_file)
#
# print(f.read())

class OurWith:
    def __enter__(self):
        print("I'm enter")

    def __exit__(self, _, _1, _2):
        print("I'm exit")

with OurWith():
    print("I'm inside with")