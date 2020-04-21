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
    #  __init__ pobranie CsvReadera i wczytanie sheeta do własnego pola -> Michał M
    def __init__(self, sheet):
        self._sheet = sheet

    # get_column -> Sabina
    def get_column(self, number):
        return [x[number] for x in self._sheet]

    # get_row -> Maksym
    def get_row(self, number):
        return self._sheet[number]

    # count_column -> Maksym
    def count_column(self):
        return len(self._sheet[0])

    # count_row -> Michał M
    def count_row(self):
        return len(self._sheet)

    # sum_column -> Sabina
    def sum_column(self, number):
        return self.apply_function_on_column(number, lambda a, b: float(a) + float(b))

    # mul_column -> Asia
    def mul_column(self, number):
        return self.apply_function_on_column(number, lambda a, b: float(a) * float(b))

    # mean_column -> Asia
    def mean_column(self, number):
        return self.sum_column(number) / self.get_row(number)

    # High order functions
    # apply_function_on_column
    def apply_function_on_column(self, number, function):
        return reduce(function, self.get_column(number))

# sheet_calculator = SheetCalculator(CsvReader("data/data.csv").get_sheet())
# print(sheet_calculator._sheet)