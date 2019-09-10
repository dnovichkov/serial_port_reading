import json

from loguru import logger


class DataParser:
    def __init__(self):
        self.parsing_results = {}

    def parse(self, arduino_string: str):
        """
        Parse data from Arduino.
        Parsed data saves
        :param arduino_string: Format: 'Sensor 1 = 56 degrees'.
        :return:
        """
        try:
            data = arduino_string.split('=')
            sensor_data = data[0]
            sensor_number = int(sensor_data.replace('Sensor ', '').strip())
            val_data = data[1]
            value = int(val_data.replace(' degrees', '').strip())
            if sensor_number not in self.parsing_results:
                self.parsing_results[sensor_number] = []
            self.parsing_results[sensor_number].append(value)
            return sensor_number, value
        except ValueError:
            logger.exception("ValueError for string {}", arduino_string)
        except IndexError:
            logger.exception("IndexError for string {}", arduino_string)
        return None

    def get_results(self):
        """
        Return parsing results.
        :return: Parsing results as dictionary {sensor_id: [measurement_values]}
        """
        return self.parsing_results

    def save_results(self, json_filename: str):
        """
        Save results in JSON-format.
        :param json_filename:
        :return:
        """
        with open(json_filename, "w") as f:
            for chunk in json.JSONEncoder(indent=4, ensure_ascii=False).iterencode(
                    self.get_results()
            ):
                f.write(chunk)
