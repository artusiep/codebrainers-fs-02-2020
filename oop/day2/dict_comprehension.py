# To see more: https://www.programiz.com/python-programming/dictionary-comprehension

# our_dict = {1: "1", 2: "2", 3: "3"}
lista_1 = [1, 2, 3, 0, 100]
lista_2 = ["1", "2", "3", "0", "dasdsa"]

print(dict(zip(lista_1, lista_2)))
print(list(zip(lista_1, lista_2, lista_1)))

list_of_tuples = [(1, 1), (2, 2)]
print(dict(list_of_tuples))

lista_3 = [1]
print(list(zip(lista_1, lista_3)))

dict_from_zip = dict(zip(lista_1, lista_2))

print(dict_from_zip.items())

x = {k*10: v for (k, v) in dict_from_zip.items() if k < 3 and v < "9"}
print(x)
