import configparser
import datetime
import sys
import os

import json

import matplotlib
import serial
import serial.tools.list_ports
from PyQt5 import QtWidgets, QtGui, QtPrintSupport
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtCore import QTime, QTimer
from loguru import logger
from serial import SerialException

from data_parser import DataParser
from data_session import DataSession
from plot_canvas import MyDynamicMplCanvas
from serial_port import Ui_MainWindow

CONFIG_FILENAME = 'settings.conf'


def get_plots_data():
    result = {}
    file_folder = os.getcwd()
    for file in os.listdir(file_folder):
        if file.endswith(".json") and file.startswith("data_"):
            plot_dt = file[5:-5]
            result[plot_dt] = file
    return result


def init_table_model(table_model: QtGui.QStandardItemModel):
    sensor_count = 8
    row0 = [QtGui.QStandardItem('Sensor ' + str(i + 1)) for i in range(0, sensor_count // 2)]
    row1 = [QtGui.QStandardItem("-") for i in range(0, sensor_count // 2)]
    row2 = [QtGui.QStandardItem('Sensor ' + str(i + 1)) for i in range(sensor_count // 2, sensor_count)]
    row3 = [QtGui.QStandardItem("-") for i in range(0, sensor_count // 2)]
    for item in row0 + row2:
        font = QtGui.QFont(item.font())
        font.setBold(True)
        item.setFont(font)
    table_model.appendRow(row0)
    table_model.appendRow(row1)
    table_model.appendRow(row2)
    table_model.appendRow(row3)


def vertical_resize_table_view_to_contents(table_view: QtWidgets.QTableView):
    row_total_height = 0

    count = table_view.verticalHeader().count()
    for i in range(0, count):
        if not table_view.verticalHeader().isSectionHidden(i):
            row_total_height += table_view.verticalHeader().sectionSize(i)
    if not table_view.horizontalScrollBar().isHidden():
        row_total_height += table_view.horizontalScrollBar().height()

    if not table_view.horizontalHeader().isHidden():
        row_total_height += table_view.horizontalHeader().height()
    table_view.setMinimumHeight(row_total_height)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.is_played = False
        self.data_session = None
        self.archive_canvas = None
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.figure_canvas = MyDynamicMplCanvas(self.ui.plot_graphics_view, width=8, height=5)
        # self.ui.main_plot_tab.set

        scene = QtWidgets.QGraphicsScene()
        self.ui.plot_graphics_view.setScene(scene)

        self.ui.actionPorts_settings.triggered.connect(self.show_dialog)

        scene.addWidget(self.figure_canvas)
        self.ui.record_button.clicked.connect(self.play_button_clicked)

        self.sensor_data_table_model = QtGui.QStandardItemModel(parent=None)
        init_table_model(self.sensor_data_table_model)

        self.ui.probe_data_table.setModel(self.sensor_data_table_model)
        vertical_resize_table_view_to_contents(self.ui.probe_data_table)
        self.ui.probe_data_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.probe_data_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.ui.probe_data_table.show()

        self.ui.measurements_list_widget.addItems(get_plots_data().keys())
        self.ui.measurements_list_widget.itemClicked.connect(self.record_clicked)
        self.ui.delete_btn.clicked.connect(self.delete_record_clicked)
        self.ui.save_btn.clicked.connect(self.record_to_pdf_clicked)
        self.ui.print_btn.clicked.connect(self.handle_print)

        self.curr_time = QTime(00, 00, 00)
        self.timer = QTimer()
        self.timer.timeout.connect(self.time)

    def time(self):
        self.curr_time = self.curr_time.addSecs(1)
        self.ui.time_label.setText(self.curr_time.toString())

    def handle_print(self):
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
        dialog = QtPrintSupport.QPrintDialog(printer, self)
        if dialog.exec_() == QtPrintSupport.QPrintDialog.Accepted:
            self.handle_paint_request(printer)

    def handle_paint_request(self, printer):
        painter = QtGui.QPainter()
        printer.setOrientation(QtPrintSupport.QPrinter.Landscape)
        painter.begin(printer)
        painter.setViewport(self.ui.plot_graphics_view_2.rect())
        painter.setWindow(self.ui.plot_graphics_view_2.rect())
        self.ui.plot_graphics_view_2.render(painter)
        painter.end()

    def get_saving_filename(self, default_name):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save plot as", default_name,
                                                            "PDF Files (*.pdf);;All Files (*)", options=options)
        return filename

    def record_to_pdf_clicked(self):
        default_filename = (
                "plot"
                + datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
                + ".pdf"
        )

        list_items = self.ui.measurements_list_widget.selectedItems()
        if not list_items:
            return
        for item in list_items:
            text = item.text()
            default_filename = 'data_' + text + '.pdf'
            break

        pdf_image_filename = self.get_saving_filename(default_filename)
        if pdf_image_filename:
            logger.debug(f'We are going to export {pdf_image_filename}')
            self.archive_canvas.save_plot(pdf_image_filename)

    def play_button_clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        if self.is_played:
            self.ui.record_button.setText("Start")
            self.curr_time = QTime(00, 00, 00)
            self.figure_canvas.stop()
            self.is_played = False
            self.data_session.stop()
            self.data_session = None
            self.ui.measurements_list_widget.clear()
            self.ui.measurements_list_widget.addItems(get_plots_data().keys())
            self.timer.stop()

        else:
            self.ui.record_button.setText("Stop")
            self.ui.time_label.setText("00:00:00")
            self.figure_canvas.run()
            self.is_played = True
            self.data_session = DataSession(self, get_config_settings())

            self.timer.start(1000)
            try:

                self.data_session.run()
            except SerialException as e:
                logger.error(f'Error while reading data: {e}')

    def add_data(self, sensor_data):
        self.statusBar().showMessage(str(sensor_data))
        self.figure_canvas.add_point(sensor_data)
        sensor_number = sensor_data[0]
        if sensor_number:
            sensor_correct = sensor_number - 1
            row_index = 2 * (sensor_correct // 4) + 1
            col_index = sensor_correct % 4
            self.sensor_data_table_model.setData(self.sensor_data_table_model.index(row_index, col_index),
                                                 sensor_data[1])

    def record_clicked(self, item):
        filename = 'data_' + item.text() + '.json'
        json_data = {}
        with open(filename, encoding='utf-8') as f:
            data = f.read()
            json_data = json.loads(data)
        if not json_data:
            logger.warning(f'File {filename} is empty')

        self.archive_canvas = MyDynamicMplCanvas(width=8, height=5)
        self.archive_canvas.line_data = json_data
        scene = QtWidgets.QGraphicsScene()
        self.ui.plot_graphics_view_2.setScene(scene)
        self.archive_canvas.update_figure()

        scene.addWidget(self.archive_canvas)

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
            logger.debug(f'Selected port is {str(text)}')
            config.set("DATA", "SERIAL_PORT", str(text))
            with open(CONFIG_FILENAME, "w") as config_file:
                config.write(config_file)

    def delete_record_clicked(self):
        list_items = self.ui.measurements_list_widget.selectedItems()
        if not list_items:
            return
        for item in list_items:
            text = item.text()
            self.ui.measurements_list_widget.takeItem(self.ui.measurements_list_widget.row(item))
            filename = 'data_' + text + '.json'
            logger.debug(f'We are going to delete {filename}')
            os.remove(filename)


matplotlib.use("Qt5Agg")


def get_config_settings():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILENAME)
    serial_port = config['DATA']['SERIAL_PORT']
    serial_rate = config['DATA']['SERIAL_RATE']
    port_settings = {'SERIAL_PORT': serial_port, 'SERIAL_RATE': serial_rate}
    return port_settings


def get_logger_level():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILENAME)
    level = config['LOGGER'].get('LEVEL', 'DEBUG')
    return level


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


def main_ui():
    app = QtWidgets.QApplication(sys.argv)

    logger.add("Serial_port_reading.log", rotation="500 MB", level=get_logger_level())
    logger.debug('Application was started')
    devices = [port.device for port in serial.tools.list_ports.comports()]
    logger.debug(f'Possible ports are: {devices}')
    win = MainWindow()
    win.show()

    app.exec_()


if __name__ == "__main__":
    # main()
    main_ui()
