import unittest

import os
import filecmp
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

    def test_bad_data(self):
        data_lines = \
            [
                'Sensor 1: 56 degrees',
                'Sensor 2 = 54 degrees ',
                'Sensor 3 = 53 degrees',
                'Sensor 3 = 52 degrees',
                'Sensor 1 = 666 degrees',
                'Sensor 1',
                'Error',
                'Sensor 1 = 666degrees',
                'Sensor 4 = No data',
            ]
        expected_result = \
            {
                1:
                    [
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

    def test_saving(self):
        data_lines = \
            [
                'Sensor 1: 56 degrees',
                'Sensor 2 = 54 degrees ',
                'Sensor 3 = 53 degrees',
                'Sensor 3 = 52 degrees',
                'Sensor 1 = 666 degrees',
                'Sensor 1',
                'Error',
                'Sensor 1 = 666degrees',
                'Sensor 4 = No data',
                'Sensor 1 = 54 degrees',
                'Sensor 1 = 55 degrees',
                'Sensor 4 = 40 degrees',
                'Sensor 3 = 55 degrees',
            ]
        parser = DataParser()
        for line in data_lines:
            parser.parse(line)
        parser.save_results('mixed_json_results.json')
        self.assertTrue(
            filecmp.cmp('mixed_json_results.json', 'json_files//mixed_json_results.json'),
            'Files are different')
        os.remove('mixed_json_results.json')
