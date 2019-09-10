import datetime
from loguru import logger
import plotly.offline
import plotly.graph_objects as go


class PlotPainter:
    def __init__(self):
        self.lines = []

    def add_data(self, data):
        pass

    @staticmethod
    def paint(plot_data):
        """
        Paint the plot and save it to html-file with name 'plot_CURRENT_TIME.html'.
        :param plot_data:
        :return:
        """
        if not isinstance(plot_data, dict):
            logger.error('Wrong plot data format')
            return

        max_len = max([len(item[1]) for item in plot_data.items()])
        logger.debug("Max plot len is {}", max_len)
        fig = go.Figure()

        fig.update_xaxes(zeroline=True)
        fig.update_yaxes(zeroline=True)

        red_line_data = [56] * max_len
        red_line_name = 'RED LINE'
        fig.add_trace(
            go.Scatter(
                y=red_line_data,
                mode='lines',
                name=red_line_name,
                line=dict(color='red', width=4)
            )
        )
        fig.update_yaxes(range=[0, 100])

        for sensor_id, values in plot_data.items():
            # Create traces
            trace_name = 'Sensor ' + str(sensor_id)
            fig.add_trace(
                go.Scatter(
                    y=values,
                    mode='lines',
                    name=trace_name,
                )
            )
        html_plot_filename = 'plot_' + datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + '.html'
        plotly.offline.plot(fig, filename=html_plot_filename)


def draw_test_plot():
    test_plot_data = \
        {
            1:
                [
                    52,
                    52,
                    54,
                    56,
                    54,
                    52,
                    55,
                ],
            2:
                [
                    54,
                    52,
                    57,
                    56,
                    55,
                    54,
                    52,
                ],
            3:
                [
                    53,
                    52,
                    54,
                    52,
                    52,
                    54,
                    52,
                ],
        }
    painter = PlotPainter()
    painter.paint(test_plot_data)


if __name__ == "__main__":
    draw_test_plot()
