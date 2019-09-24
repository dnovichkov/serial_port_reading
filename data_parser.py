import json
import datetime

from loguru import logger


class DataParser:
    def __init__(self, params):
        self.parsing_results = {}
        self.params = params
        self.start_time = datetime.datetime.now().strftime("%d.%m.%Y %H-%M-%S")

    def parse(self, arduino_string: str):
        """
        Parse data from Arduino.
        Parsed data saves
        :param arduino_string: Format: 'Temperature1=56'.
        :return: None if arduino_string and (Sensor_number, value) if everything is correct.
        """
        try:
            data = arduino_string.split('=')
            sensor_data = data[0]
            sensor_number = int(sensor_data.replace('Temperature', '').strip())
            value = int(data[1])
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
        stop_time = datetime.datetime.now().strftime("%d.%m.%Y %H-%M-%S")
        self.params['range'] = self.start_time + ' - ' + stop_time
        return {'points': self.parsing_results, 'params': self.params}

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
