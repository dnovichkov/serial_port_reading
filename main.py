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

from serial_port import Ui_MainWindow

CONFIG_FILENAME = 'settings.conf'


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.is_played = False
        self.figure_canvas = MyDynamicMplCanvas()
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        scene = QtWidgets.QGraphicsScene()
        self.ui.plot_graphics_view.setScene(scene)

        self.ui.actionPorts_settings.triggered.connect(self.show_dialog)

        scene.addWidget(self.figure_canvas)
        self.ui.record_button.clicked.connect(self.play_button_clicked)

        sensor_data_table_model = QtGui.QStandardItemModel(parent=None)
        sensor_count = 8
        headers = ['Sensor ' + str(i) for i in range(0, sensor_count)]
        row = [QtGui.QStandardItem(50 + i) for i in range(0, sensor_count)]

        sensor_data_table_model.setHorizontalHeaderLabels(headers)
        sensor_data_table_model.appendRow(row)

        self.ui.probe_data_table.setModel(sensor_data_table_model)
        self.ui.probe_data_table.show()

    def play_button_clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        if self.is_played:
            self.ui.record_button.setText("Play")
            self.is_played = False
            self.figure_canvas.stop()
        else:
            self.ui.record_button.setText("Stop")
            self.is_played = True
            self.figure_canvas.start()

    def show_dialog(self):
        devices = [port.device for port in serial.tools.list_ports.comports()]
        config = configparser.ConfigParser()
        config.read(CONFIG_FILENAME)
        serial_port = config['DATA']['SERIAL_PORT']
        if not devices:
            devices.append(serial_port)
            message_string = f'Warning: no ports in system, use value from config: {serial_port}'
            self.statusBar().showMessage(message_string)

        text, ok = QInputDialog.getItem(None, "Port setting", "Choose port:", devices, 0, False)

        if ok and text:
            config.set("DATA", "SERIAL_PORT", str(text))
            with open(CONFIG_FILENAME, "w") as config_file:
                config.write(config_file)

matplotlib.use("Qt5Agg")


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
    win = MainWindow()
    win.show()

    app.exec_()


if __name__ == "__main__":
    # main()
    main_ui()
