import serial
from loguru import logger

from data_parser import DataParser

DEFAULT_PORT_SETTINGS = {'SERIAL_PORT': 'COM1', 'SERIAL_RATE': 9600}


class DataReader:
    def __init__(self, port, rate, session):
        self.port = port
        self.rate = rate
        self.session = session

    def run(self):
        # TODO: run reading in different thread
        ser = serial.Serial(self.port, self.rate)
        while True:
            try:
                reading = ser.readline().decode('utf-8')
                logger.debug(reading)
                self.session.add_data(reading)
            except KeyboardInterrupt:
                # FIXME: add STOP-method
                print("Keyboard Interrupt")


class DataSession:
    def __init__(self, plot_painter, port_settings=DEFAULT_PORT_SETTINGS):
        self.data_parser = DataParser()
        self.plot_painter = plot_painter
        self.port_settings = port_settings

    def run(self):
        serial_port = self.port_settings.get('SERIAL_PORT')
        serial_rate = self.port_settings.get('SERIAL_RATE')
        reader = DataReader(serial_port, serial_rate, self)
        reader.run()

    def add_data(self, sensor_data: str):
        sensor_data = self.data_parser.parse(sensor_data)
        if sensor_data:
            self.plot_painter.add_data(sensor_data)
            # TODO: save to DB
