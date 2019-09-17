import time

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
        logger.debug(f'Run {self.is_started}')
        while True and self.is_started:
            logger.debug(f'Run in cycle {self.is_started}')
            time.sleep(1)
            reading = self.serial_device.readline().decode('utf-8')
            logger.debug(reading)
            self.read_data_signal.emit(reading)

    @pyqtSlot()
    def stop(self):
        logger.debug('SerialWorker stop')
        self.is_started = False
        self.serial_device.close()


class DataSession(QObject):
    signal_start_background_job = pyqtSignal()
    signal_stop_background_job = pyqtSignal()

    def __init__(self, plot_painter, port_settings=DEFAULT_PORT_SETTINGS):
        super().__init__()
        self.data_parser = DataParser()
        self.plot_painter = plot_painter

        self.worker = SerialWorker(port_settings)
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.worker.read_data_signal.connect(self.add_data)

        self.signal_start_background_job.connect(self.worker.run)
        self.signal_stop_background_job.connect(self.worker.stop)

    def start_background_job(self):
        self.thread.start()
        self.signal_start_background_job.emit()

    def run(self):
        self.start_background_job()

    @pyqtSlot()
    def add_data(self, sensor_data: str):
        logger.debug(sensor_data)
        sensor_data = self.data_parser.parse(sensor_data)
        if sensor_data:
            self.plot_painter.add_data(sensor_data)
            # TODO: save to DB

    def stop(self):
        self.worker.stop()
        self.thread.quit()
        self.thread.wait(1000)
