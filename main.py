import configparser
import datetime
import sys

import matplotlib.pylab as plt
import numpy as np
import serial
from PyQt5 import QtWidgets, uic
from loguru import logger
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from data_parser import DataParser
from plot_painter import PlotPainter


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
    win = uic.loadUi("serial_port.ui")  # specify the location of your .ui file
    win.show()

    scene = QtWidgets.QGraphicsScene()
    win.plot_graphics_view.setScene(scene)

    fig, ax1 = plt.subplots()
    plot_widget = FigureCanvas(fig)
    x = np.linspace(0, 10 * np.pi, 100)
    y = np.sin(x)

    line1, = ax1.plot(x, y, 'b-')

    for phase in np.linspace(0, 10 * np.pi, 100):
        line1.set_ydata(np.sin(0.5 * x + phase))
    fig.canvas.draw()

    scene.addWidget(plot_widget)

    app.exec_()


if __name__ == "__main__":
    # main()
    main_ui()
