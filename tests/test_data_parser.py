import unittest
from data_parser import DataParser


class TestDataParser(unittest.TestCase):
    def test_good_data(self):
        data_lines = \
            [
                'Sensor 1 = 56 degrees',
                'Sensor 2 = 54 degrees ',
                'Sensor 3 = 53 degrees',
                'Sensor 3 = 52 degrees',
                'Sensor 1 = 666 degrees',
            ]
        expected_result = \
            {
                1:
                    [
                        56,
                        666
                    ],
                2:
                    [
                        54
                    ],
                3:
                    [
                        53,
                        52
                    ],
            }

        parser = DataParser()
        for line in data_lines:
            parser.parse(line)
        parsing_results = parser.get_results()
        self.assertEqual(expected_result, parsing_results)
