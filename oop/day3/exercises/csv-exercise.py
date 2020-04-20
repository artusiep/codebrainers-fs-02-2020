# Example CSV http://siepietowski.pl/course/data.csv
import csv
from functools import reduce


class CsvReader:
    # __init__ wczytanie pliku csv poprzez podanie scieżki + stworzenie 2 pól _path, _sheet (2d list)
    # get_sheet zwórcenie sheeta
    def __init__(self, filepath):
        self._path = filepath
        with open(self._path) as file:
            temp = csv.reader(file)
            self._sheet = list(temp)[1:]

    def get_sheet(self):
        return self._sheet


class SheetCalculator:
    def __init__(self, sheet):
        self._sheet = sheet

    #  __init__ pobranie CsvReadera i wczytanie sheeta do własnego pola -> Michał M
    # get_column -> Sabina
    # get_row -> Maksym
    # count_column -> Maksym
    # count_row -> Michał M
    # sum_column -> Sabina
    # mul_column -> Asia
    # mean_column -> Asia
    def get_column(self, number):
        return [x[number] for x in self._sheet]

    # High order functions
    def apply_function_on_column(self, number, function):
        return reduce(function, self.get_column(number))

    # apply_function_on_column

sheet_calculator = SheetCalculator(CsvReader("data/data.csv").get_sheet())
print(sheet_calculator.apply_function_on_column(1, lambda x, y: x+y))
print(sheet_calculator.apply_function_on_column(6, lambda x, y: int(x)+int(y)))
print(sheet_calculator.apply_function_on_column(6, lambda x, y: int(y)))
