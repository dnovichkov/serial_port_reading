import configparser
import datetime
import json
import os

import serial
from PyQt5 import QtGui, QtPrintSupport, QtWidgets
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QInputDialog
from loguru import logger
from serial import SerialException

from data_session import DataSession
from plot_canvas import MyDynamicMplCanvas
from serial_port import Ui_MainWindow

CONFIG_FILENAME = 'settings.conf'


def get_config_settings():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILENAME)
    serial_port = config['DATA']['SERIAL_PORT']
    serial_rate = config['DATA']['SERIAL_RATE']
    port_settings = {'SERIAL_PORT': serial_port, 'SERIAL_RATE': serial_rate}
    return port_settings


def get_ui_settings():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILENAME)
    items = {key: os.getenv(key, value) for key, value in config.items('GUI')}
    return items


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.is_played = False
        self.data_session = None
        self.archive_canvas = None
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_text_fields()
        self.figure_canvas = MyDynamicMplCanvas(self.ui.plot_graphics_view, width=10, height=5)
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
        self.time_update_timer = QTimer()
        self.time_update_timer.timeout.connect(self.update_time)

        self.stop_timer = QTimer()
        self.stop_timer.setSingleShot(True)
        self.stop_timer.timeout.connect(self.stop_reading)

    def closeEvent(self, event):
        logger.debug("Last windows closed, exiting ...")
        params = self.get_params()
        params.pop('duration', None)

        config = configparser.ConfigParser()

        config.read(CONFIG_FILENAME)
        try:
            for name, value in params.items():
                config.set("GUI", name, str(value))
            with open(CONFIG_FILENAME, "w") as config_file:
                config.write(config_file)
        except:
            logger.warning("Error while saving GUI settings")
        super(MainWindow, self).closeEvent(event)

    def update_time(self):
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
            self.stop_reading()

        else:
            self.run_reading()

    def get_duration(self):
        durations_map = \
            {
                '24h': 24 * 60 * 60,
                '12h': 12 * 60 * 60,
                '1h': 60 * 60,
            }
        duration_label_value = self.ui.measument_durtion_combo_box.currentText()
        default_duration = 60 * 60
        duration = durations_map.get(duration_label_value, default_duration)
        return duration

    def get_params(self):
        result = \
            {
                'duration': self.get_duration(),
                'company': self.ui.company_input.toPlainText(),
                'id': self.ui.id_input.toPlainText(),
                'location': self.ui.location_input.toPlainText(),
                'country': self.ui.country_input.toPlainText(),
                'load_number_id': self.ui.load_number_id_input.toPlainText(),
                'registrated_number': self.ui.registrated_number_input.toPlainText(),
                'treatment_location': self.ui.treatment_location_input.toPlainText(),
                'type_of_material': self.ui.type_of_material_input.toPlainText(),
                'quantity': self.ui.quantity_inpeu.toPlainText(),
                'verification': self.ui.verificaion_input.toPlainText(),
                'note': self.ui.note_iinput.toPlainText(),
            }
        return result

    def init_text_fields(self):
        gui_params = get_ui_settings()
        self.ui.company_input.insertPlainText(gui_params.get('company'))
        self.ui.location_input.insertPlainText(gui_params.get('location'))
        self.ui.country_input.insertPlainText(gui_params.get('country'))
        self.ui.id_input.insertPlainText(gui_params.get('id'))
        self.ui.load_number_id_input.insertPlainText(gui_params.get('load_number_id'))
        self.ui.registrated_number_input.insertPlainText(gui_params.get('registrated_number'))

        self.ui.treatment_location_input.insertPlainText(gui_params.get('treatment_location'))
        self.ui.type_of_material_input.insertPlainText(gui_params.get('type_of_material'))
        self.ui.quantity_inpeu.insertPlainText(gui_params.get('quantity'))
        self.ui.verificaion_input.insertPlainText(gui_params.get('verification'))
        self.ui.note_iinput.insertPlainText(gui_params.get('note'))

    def run_reading(self):
        self.ui.record_button.setText("Stop")
        self.ui.time_label.setText("00:00:00")

        duration = self.get_duration()
        self.figure_canvas.run(duration)
        self.is_played = True
        self.data_session = DataSession(self, self.get_params(), get_config_settings())
        self.time_update_timer.start(1000)
        self.stop_timer.start((duration + 1) * 1000)
        try:

            self.data_session.run()
        except SerialException as e:
            logger.error(f'Error while reading data: {e}')

    def stop_reading(self):
        self.ui.record_button.setText("Start")
        self.curr_time = QTime(00, 00, 00)
        self.figure_canvas.stop()
        self.is_played = False
        self.data_session.stop()
        self.data_session = None
        self.ui.measurements_list_widget.clear()
        self.ui.measurements_list_widget.addItems(get_plots_data().keys())
        self.time_update_timer.stop()
        self.stop_timer.stop()

    def add_data(self, sensor_data):
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

        self.archive_canvas = MyDynamicMplCanvas(width=10, height=8)
        self.archive_canvas.line_data = json_data.get('points')
        self.archive_canvas.duration = json_data.get('params', {}).get('duration', 0)
        self.archive_canvas.params = json_data.get('params')
        # if json_data:
        #     lens = [len(x) for x in json_data.values()]
        #     print(max(lens))
        #     # self.archive_canvas.red_points = {0: 56, self.duration / 3600: 56}
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
