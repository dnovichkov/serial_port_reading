import unittest

import os
import filecmp
from data_parser import DataParser


class TestDataParser(unittest.TestCase):
    def test_good_data(self):
        data_lines = \
            [
                'Temperature1=56',
                'Temperature2=54 ',
                'Temperature3=53',
                'Temperature3=52',
                'Temperature1=666',
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
                'Temperature1: 56',
                'Temperature2=54 ',
                'Temperature3=53',
                'Temperature3=52',
                'Temperature1=666',
                'Temperature1',
                'Error',
                'Temperature1=666degrees',
                'Temperature4=No data',
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
                'Temperature1: 56',
                'Temperature2=54 ',
                'Temperature3=53',
                'Temperature3=52',
                'Temperature1=666',
                'Temperature1',
                'Error',
                'Temperature1=666degrees',
                'Temperature4=No data',
                'Temperature1=54',
                'Temperature1=55',
                'Temperature4=40',
                'Temperature3=55',
            ]
        parser = DataParser()
        for line in data_lines:
            parser.parse(line)
        parser.save_results('mixed_json_results.json')
        self.assertTrue(
            filecmp.cmp('mixed_json_results.json', 'json_files//mixed_json_results.json'),
            'Files are different')
        os.remove('mixed_json_results.json')
