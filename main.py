import configparser
import datetime
import sys

import matplotlib
import serial
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QInputDialog
from loguru import logger

from data_parser import DataParser
from plot_canvas import MyDynamicMplCanvas
from plot_painter import PlotPainter

matplotlib.use("Qt5Agg")


def show_dialog():
    text, ok = QInputDialog.getText(None, 'Port settings',
                                    'Enter port')

    if ok:
        print(str(text))


def main():
    config = configparser.ConfigParser()
    config.read('settings.conf')
    serial_port = config['DATA']['SERIAL_PORT']
    serial_rate = config['DATA']['SERIAL_RATE']

    logger.add("file_{time}.log")
    logger.debug("We've run reading from serial port")
    logger.debug('SERIAL_RATE is {}', serial_port)
    logger.debug('SERIAL_PORT is {}', serial_rate)

    ser = serial.Serial(serial_port, serial_rate)
    data_parser = DataParser()

    while True:
        try:
            reading = ser.readline().decode('utf-8')
            logger.debug(reading)
            data_parser.parse(reading)
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            json_file_name = (
                    "test_data"
                    + str(serial_port)
                    + "_"
                    + datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
                    + "_result.json"
            )
            data_parser.save_results(json_file_name)
            painter = PlotPainter()
            painter.paint(data_parser.get_results())


def main_ui():
    app = QtWidgets.QApplication(sys.argv)
    win = uic.loadUi("serial_port.ui")
    win.show()

    scene = QtWidgets.QGraphicsScene()
    win.plot_graphics_view.setScene(scene)

    win.actionPorts_settings.triggered.connect(show_dialog)

    dc = MyDynamicMplCanvas()
    scene.addWidget(dc)

    app.exec_()


if __name__ == "__main__":
    # main()
    main_ui()
