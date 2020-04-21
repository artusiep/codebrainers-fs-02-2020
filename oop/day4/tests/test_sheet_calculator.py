import unittest

from oop.day4.csv_exercise import SheetCalculator


# test suit - testuje całą klasę w tym wypadku
class TestSheetCalculator(unittest.TestCase):
    # test case = testuje jedną metodę
    def test_get_column(self):
        # GIVEN (dane wejściowe)
        sheet_calculator = SheetCalculator([
            ['column1', 'column2', 'column3'],
            [1, 2, 3]
        ])
        expected_result = ['column3', 3]
        argument = 2
        # WHEN (operacja)
        result = sheet_calculator.get_column(argument)
        # THEN
        # 1 sposób stary
        # assert result == expected_result
        # 2 sposób
        self.assertEqual(result, expected_result)
        # 3 sposób ale przedawniony
        # self.assertEquals(result, expected_result)

    def test_get_column_index_out_of_range(self):
        # GIVEN
        sheet_calculator = SheetCalculator([
            ['column1', 'column2', 'column3'],
            [1, 2, 3]
        ])
        expected_result = None
        argument = 4
        # WHEN/THEN
        with self.assertRaises(IndexError) as exception:
            result = sheet_calculator.get_column(argument)
        # # THEN
        # print(exception)

    def test_get_column_index_minus(self):
        # GIVEN
        sheet_calculator = SheetCalculator([
            ['column1', 'column2', 'column3'],
            [1, 2, 3]
        ])
        expected_result = ['column3', 3]
        argument = -1
        # WHEN
        result = sheet_calculator.get_column(argument)
        # THEN
        self.assertEqual(expected_result, result)

    def test_get_row(self):
        pass
        # GIVEN
        sheet_calculator = SheetCalculator([
            ['column1', 'column2', 'column3'],
            [1, 2, 3]
        ])
        expected_result_row = [1, 2, 3]
        expected_result_len = 3
        argument = 1
        # WHEN
        result_row = sheet_calculator.get_row(argument)
        result_len = len(sheet_calculator.get_row(argument))
        # THEN
        self.assertEqual(expected_result_row, result_row)
        self.assertEqual(expected_result_len, result_len)
