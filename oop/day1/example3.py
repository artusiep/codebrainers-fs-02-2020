numbers = []
numbers.append("1")
numbers.append("2")
list
print(numbers)

# Nadpisywanie metod
class Pies:
    def szczekaj(self):
        print("MIAŁ MIAŁ")


def moje_szczekaj(_):
    print("HAU HAU")


# Pies.szczekaj = moje_szczekaj

obiekt_pies = Pies()
obiekt_pies.szczekaj()