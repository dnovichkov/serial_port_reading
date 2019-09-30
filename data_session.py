import time
import copy
import datetime

import serial
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread
from loguru import logger
from serial import SerialException

from data_parser import DataParser

DEFAULT_PORT_SETTINGS = {'SERIAL_PORT': 'COM1', 'SERIAL_RATE': 9600}


class ReadLine:
    def __init__(self, s):
        self.buf = bytearray()
        self.s = s

    def readline(self):
        i = self.buf.find(b"\n")
        if i >= 0:
            r = self.buf[:i + 1]
            self.buf = self.buf[i + 1:]
            return r
        while True:
            i = max(1, min(2048, self.s.in_waiting))
            data = self.s.read(i)
            i = data.find(b"\n")
            if i >= 0:
                r = self.buf + data[:i + 1]
                self.buf[0:] = data[i + 1:]
                return r
            else:
                self.buf.extend(data)


class SerialWorker(QObject):
    """
    Worker for non-blocking reading data from serial port.
    """
    read_data_signal = pyqtSignal(str)

    def __init__(self, port_settings):

        super().__init__()
        self.is_started = True
        port = port_settings['SERIAL_PORT']
        rate = port_settings['SERIAL_RATE']
        logger.debug(f'Open port {port} with rate {rate}')
        try:
            self.serial_device = serial.Serial(port, rate)
            self.serial_device.flushInput()
        except SerialException as e:
            logger.error(f'Error while reading: {e}')

    @pyqtSlot()
    def run(self):
        while self.is_started:
            if self.serial_device.is_open:
                rl = ReadLine(self.serial_device)
                line = rl.readline().decode('utf-8')
                logger.debug(line)
                self.read_data_signal.emit(line)

        logger.debug("We finished reading")

    def stop(self):
        self.is_started = False
        self.serial_device.close()


class DataSession(QObject):
    signal_start_background_job = pyqtSignal()

    def __init__(self, plot_painter, params, port_settings=DEFAULT_PORT_SETTINGS):
        super().__init__()

        self.data_parser = DataParser(params)
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

    def stop(self, additional_params):
        self.worker.stop()
        self.thread.quit()
        self.thread.wait(1000)
        json_file_name = (
                "data_"
                + datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
                + ".json"
        )
        self.data_parser.save_results(json_file_name, additional_params)
