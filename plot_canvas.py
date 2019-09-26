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
        7: '#7fff00',
        8: '#ff00ff',
    }

DEFAULT_COLOR = '#008080'


class MyDynamicMplCanvas(FigureCanvas):
    """A canvas that updates itself every second with a new plot."""

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
        self.line_data = {}

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_figure)
        self.red_points = {}
        self.params = {}
        self.duration = 0

    def compute_initial_figure(self):
        pass

    def add_point(self, point):
        logger.debug(f'Add point {point} to plot')
        sensor_id = point[0]
        if sensor_id not in self.line_data:
            self.line_data[sensor_id] = []
        self.line_data[sensor_id].append(point[1])

    def set_duration(self, duration):
        self.duration = duration
        self.fig.gca().set_ylim([0, 100])
        self.fig.gca().set_xlim([0, self.duration / 3600])
        self.draw()

    def run(self, duration):
        self.axes.clear()
        self.line_data = {}
        self.set_duration(duration)
        self.timer.start(1000)

    def stop(self):
        self.timer.stop()
        self.duration = 0

    def get_titles(self):
        titles = {}
        title_1 = f'Type of material: {self.params.get("type_of_material", "-")}\n' \
                  f'Quantity: {self.params.get("quantity", "-")}\n' \
                  f'Location: {self.params.get("location", "-")}\n' \
                  f'Load ID: {self.params.get("load_number_id", "-")}\n' \
                  f'Time of treatment: {self.params.get("range", "-")}'
        titles['left'] = title_1

        title_2 = f'Reference temperature: 56°C\n' \
                  f'Period above ref. temp.: ???\n' \
                  f'Beginning: {self.params.get("start", "-")}\n' \
                  f'End: {self.params.get("finish", "-")}'
        titles['center'] = title_2
        title_3 = f'Company: {self.params.get("company", "-")}\n' \
                  f'ID: {self.params.get("id", "-")}\n' \
                  f'Registrated number: {self.params.get("registrated_number", "-")}\n' \
                  f'Address: {self.params.get("address", "-")}\n'\
                  f'Country: {self.params.get("country", "-")}'
        titles['right'] = title_3

        return titles

    def update_figure(self):
        self.axes.clear()
        self.fig.gca().set_ylim([0, 101])

        major_ticks = range(0, 101, 10)
        minor_ticks = range(0, 101, 5)
        self.fig.gca().set_yticks(major_ticks)
        self.fig.gca().set_yticks(minor_ticks, minor=True)
        # self.fig.gca().grid(True)

        if self.duration == 24 * 3600:
            self.fig.gca().set_xticks(range(0, 25, 1))
        elif self.duration == 12 * 3600:
            self.fig.gca().set_xticks(range(0, 13, 1))
        elif self.duration == 3600:

            major_x_ticks = range(0, 61, 10)
            minor_x_ticks = range(0, 61, 5)
            self.fig.gca().set_xticks(major_x_ticks)
            self.fig.gca().set_xticks(minor_x_ticks, minor=True)

            # self.fig.gca().set_xticks(range(0, 61, 1))

        self.fig.gca().grid(which='both')
        self.fig.gca().grid(which='minor', alpha=0.2)
        self.fig.gca().grid(which='major', alpha=0.5)

        if self.duration:
            duration_in_hours = self.duration / 3600
            self.fig.gca().set_xlim([0, duration_in_hours])
        if self.duration == 3600:
            self.fig.gca().set_xlim([0, 61])

        self.red_points = {0: 56, self.duration / 3600: 56}
        if self.duration == 3600:
            self.red_points[60] = 56
        self.axes.plot(
            list(self.red_points.keys()), list(self.red_points.values()),
            'r', label='ref. temp', linewidth=1.0,
            antialiased=True)

        for id_, points in self.line_data.items():
            color = PLOT_COLORS.get(int(id_), DEFAULT_COLOR)
            plot_count = len(points)
            name = f'temp.{id_}'
            if self.duration == 3600:
                x_coords = [x / 60 for x in range(plot_count)]
            else:
                x_coords = [x / 3600 for x in range(plot_count)]
            self.axes.plot(x_coords, points, color, label=name)

        self.fig.legend(loc='lower center', shadow=False, ncol=5, framealpha=0.4)
        if self.params:
            titles = self.get_titles()
            for location, title in titles.items():
                self.fig.gca().set_title(title, loc=location, wrap=True, fontsize=10)
            device_text = 'Measuring device: HT15\nManufacturer: DOO Draft'
            x_coord_for_text = -8
            x_coord_for_person = 55
            if self.duration == 3600 * 12:
                x_coord_for_text = -1.6
                x_coord_for_person = 11
            if self.duration == 3600 * 24:
                x_coord_for_text = -3.2
                x_coord_for_person = 22
            self.axes.text(x_coord_for_text, -10, device_text,
                           {'color': 'black', 'fontsize': 9, 'ha': 'left', 'va': 'center', })
            person_text = '______________________\nPerson responsible'
            self.axes.text(x_coord_for_person, -10, person_text,
                           {'color': 'black', 'fontsize': 9, 'ha': 'center', 'va': 'center', })
        self.draw()

    def save_plot(self, filename: str):
        self.fig.savefig(filename)
