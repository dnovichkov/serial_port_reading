import random

from loguru import logger

import matplotlib

from PyQt5 import QtCore
from PyQt5.QtWidgets import QSizePolicy

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

matplotlib.use("Qt5Agg")


PLOT_COLORS = \
    {
        1: 'b',
        2: 'g',
        3: 'c',
        4: 'm',
        5: 'y',
        6: 'k',
        7: 'w',
        8: '#ff00ff',
    }

DEFAULT_COLOR = '#008080'


class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=6, height=5, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        self.line_data = {}

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_figure)
        self.red_points = {}
        self.duration = 0

    def add_point(self, point):
        logger.debug(f'Add point {point} to plot')
        sensor_id = point[0]
        if sensor_id not in self.line_data:
            self.line_data[sensor_id] = []
        self.line_data[sensor_id].append(point[1])

    def run(self, duration):
        self.axes.clear()
        self.duration = duration
        self.fig.gca().set_ylim([0, 100])
        self.fig.gca().set_xlim([0, self.duration / 3600])
        self.line_data = {}
        self.draw()
        self.timer.start(1000)

    def stop(self):
        self.timer.stop()
        self.duration = 0

    def update_figure(self):
        self.axes.clear()
        self.fig.gca().set_ylim([0, 100])
        if self.duration:
            self.fig.gca().set_xlim([0, self.duration / 3600])
        for id_, points in self.line_data.items():
            color = PLOT_COLORS.get(int(id_), DEFAULT_COLOR)
            plot_count = len(points)
            name = f'Temp_{id_}'
            x_coords = [x / 3600 for x in range(plot_count)]
            self.axes.plot(x_coords, points, color, label=name)

        self.red_points = {0: 56, self.duration / 3600: 56}
        if self.red_points:
            self.axes.plot(list(self.red_points.keys()), list(self.red_points.values()), 'r', label='RED_LINE')
        self.fig.legend(loc='lower center', shadow=True, ncol=2)
        self.draw()

    def save_plot(self, filename: str):
        self.fig.savefig(filename)
