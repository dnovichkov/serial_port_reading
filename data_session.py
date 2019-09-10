import configparser

import serial
from loguru import logger

from data_parser import DataParser
from plot_painter import PlotPainter


class DataSession:
    def __init__(self):
        self.data_parser = DataParser()
        self.plot_painter = PlotPainter()

    def run(self):

        # TODO: run reading in different thread
        config = configparser.ConfigParser()
        config.read('settings.conf')
        serial_port = config['DATA']['SERIAL_PORT']
        serial_rate = config['DATA']['SERIAL_RATE']

        ser = serial.Serial(serial_port, serial_rate)
        while True:
            try:
                reading = ser.readline().decode('utf-8')
                logger.debug(reading)
                self.data_parser.parse(reading)
            except KeyboardInterrupt:
                print("Keyboard Interrupt")

    def add_data(self, sensor_data):
        self.plot_painter.add_data(sensor_data)
