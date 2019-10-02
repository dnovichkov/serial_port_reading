import configparser
import sys
import platform


import matplotlib
import serial
import serial.tools.list_ports
from PyQt5 import QtWidgets
from loguru import logger

from main_window import MainWindow

CONFIG_FILENAME = 'settings.conf'

matplotlib.use("Qt5Agg")


def get_logger_level():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILENAME)
    level = config['LOGGER'].get('LEVEL', 'DEBUG')
    return level


def main_ui():
    app = QtWidgets.QApplication(sys.argv)

    logger.add("Serial_port_reading.log", rotation="500 MB", level=get_logger_level())
    logger.debug('Application was started, version is 2019-10-01 15:16')
    logger.debug(f"Machine: {platform.machine()}")
    logger.debug(f"version: {platform.version()}")
    logger.debug(f"platform: {platform.platform()}")
    logger.debug(f"uname: {platform.machine()}")
    logger.debug(f"system: {platform.system()}")
    devices = [port.device for port in serial.tools.list_ports.comports()]
    logger.debug(f'Possible ports are: {devices}')
    win = MainWindow()
    win.show()

    app.exec_()


if __name__ == "__main__":
    # main()
    main_ui()
