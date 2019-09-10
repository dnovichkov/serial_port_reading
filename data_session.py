from threading import Thread

import serial
from loguru import logger

from data_parser import DataParser

DEFAULT_PORT_SETTINGS = {'SERIAL_PORT': 'COM1', 'SERIAL_RATE': 9600}


def run_read(serial_device: serial.Serial, session):
    while True:
        reading = serial_device.readline().decode('utf-8')
        logger.debug(reading)
        session.add_data(reading)


class DataSession:
    def __init__(self, plot_painter, port_settings=DEFAULT_PORT_SETTINGS):
        self.data_parser = DataParser()
        self.plot_painter = plot_painter
        self.port_settings = port_settings
        self.reading_thread = None

    def run(self):
        ser = serial.Serial(self.port, self.rate)
        self.reading_thread = Thread(target=run_read, args=(ser, self))
        self.reading_thread.start()

    def add_data(self, sensor_data: str):
        sensor_data = self.data_parser.parse(sensor_data)
        if sensor_data:
            self.plot_painter.add_data(sensor_data)
            # TODO: save to DB

    def stop(self):
        if self.reading_thread:
            self.reading_thread.join()
            self.reading_thread = None
