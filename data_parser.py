class DataParser:
    def __init__(self):
        self.parsing_results = {}

    def parse(self, arduino_string: str):
        data = arduino_string.split('=')
        sensor_data = data[0]
        sensor_number = int(sensor_data.replace('Sensor ', '').strip())
        if sensor_number not in self.parsing_results:
            self.parsing_results[sensor_number] = []
        val_data = data[1]
        value = int(val_data.replace(' degrees', '').strip())
        self.parsing_results[sensor_number].append(value)

    def get_results(self):
        return self.parsing_results
