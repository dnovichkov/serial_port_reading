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

    def add_point(self, point):
        logger.debug(f'Add point {point} to plot')
        sensor_id = point[0]
        if sensor_id not in self.line_data:
            self.line_data[sensor_id] = []
        self.line_data[sensor_id].append(point[1])
        self.update_figure()

    def run(self):
        self.axes.clear()
        self.line_data = {}
        self.draw()

    def update_figure(self):
        self.axes.clear()
        max_point_count = 0
        for id_, points in self.line_data.items():
            color = PLOT_COLORS.get(id_, DEFAULT_COLOR)
            plot_count = len(points)
            max_point_count = max(max_point_count, plot_count)
            name = f'Temp_{id_}'
            self.axes.plot(range(plot_count), points, color, label=name)
        if max_point_count:
            red = [56 for i in range(max_point_count)]
            self.axes.plot(range(max_point_count), red, 'r', label='RED_LINE')
        self.fig.legend(loc='lower center', shadow=True, ncol=2)
        self.draw()

    def save_plot(self, filename: str):
        self.fig.savefig(filename)
