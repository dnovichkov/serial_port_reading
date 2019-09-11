import configparser
import datetime
import sys

import matplotlib
import serial
import serial.tools.list_ports
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QInputDialog
from loguru import logger

from data_parser import DataParser
from plot_canvas import MyDynamicMplCanvas
from plot_painter import PlotPainter

matplotlib.use("Qt5Agg")


def show_dialog():
    devices = [port.device for port in serial.tools.list_ports.comports()]
    text, ok = QInputDialog.getText(None, 'Port settings',
                                    'Enter port. Possible values: {0}'.format(devices))
    # TODO: Rework text to spinbox
    # TODO: Save value to config-file

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

    figure_canvas = MyDynamicMplCanvas()
    scene.addWidget(figure_canvas)
    win.record_button.clicked.connect(figure_canvas.start)

    # Fixme: ugly design.
    sensor_data_table_model = QtGui.QStandardItemModel(parent=app)
    sensor_count = 8
    headers = ['Sensor ' + str(i) for i in range(0, sensor_count)]
    row = [QtGui.QStandardItem(50 + i) for i in range(0, sensor_count)]

    sensor_data_table_model .setHorizontalHeaderLabels(headers)
    sensor_data_table_model .appendRow(row)

    win.probe_data_table.setModel(sensor_data_table_model )
    win.probe_data_table.show()

    app.exec_()


if __name__ == "__main__":
    # main()
    main_ui()
