import time
import copy

import serial
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread
from loguru import logger
from serial import SerialException

from data_parser import DataParser

DEFAULT_PORT_SETTINGS = {'SERIAL_PORT': 'COM1', 'SERIAL_RATE': 9600}


class SerialWorker(QObject):
    read_data_signal = pyqtSignal(str)

    def __init__(self, port_settings):

        super().__init__()
        self.is_started = True
        port = port_settings['SERIAL_PORT']
        rate = port_settings['SERIAL_RATE']
        logger.debug(f'Open port {port} with rate {rate}')
        try:
            self.serial_device = serial.Serial(port, rate)
        except SerialException as e:
            logger.error(f'Error while reading: {e}')

    @pyqtSlot()
    def run(self):
        while self.is_started:
            time.sleep(1)
            line = self.serial_device.readline().decode('utf-8')
            logger.debug(line)
            data_copy = copy.deepcopy(line)
            self.read_data_signal.emit(data_copy)

        logger.debug("We finished reading")

    def stop(self):
        self.is_started = False
        self.serial_device.close()


class DataSession(QObject):
    signal_start_background_job = pyqtSignal()

    def __init__(self, plot_painter, port_settings=DEFAULT_PORT_SETTINGS):
        super().__init__()

        self.data_parser = DataParser()
        self.plot_painter = plot_painter

        self.worker = SerialWorker(port_settings)
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.worker.read_data_signal.connect(self.add_data)
        self.signal_start_background_job.connect(self.worker.run)

    def run(self):
        self.thread.start()
        self.signal_start_background_job.emit()

    def add_data(self, sensor_data):
        logger.debug(f"Data was read: {sensor_data}")
        parser_data = self.data_parser.parse(sensor_data)
        if parser_data:
            self.plot_painter.add_data(parser_data)
            # TODO: save to DB

    def stop(self):
        self.worker.stop()
        self.thread.quit()
        self.thread.wait(1000)
