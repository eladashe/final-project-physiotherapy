import numpy as np
import pandas as pd
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QSizePolicy
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.ticker import PercentFormatter

class GraphManager:
    def __init__(self, parent_widget: QWidget):
        self.parent_widget = parent_widget
        self.layout = parent_widget.layout() or QGridLayout()
        if parent_widget.layout() is None:
            parent_widget.setLayout(self.layout)
        self.canvases = {}

    def get_or_create_canvas(self, key: str, figsize=(5, 3)) -> Figure:
        if key in self.canvases:
            # Delete previous canvas
            canvas = self.canvases[key]
            fig = Figure(figsize=figsize)
            if canvas:
                canvas.setParent(None)
                del self.canvases[key]

        # Create a new figure
        fig = Figure(figsize=(5, 3))
        canvas = FigureCanvas(fig)

        # Make sure the canvas takes up all the space
        canvas.setMinimumSize(self.parent_widget.width(), self.parent_widget.height())
        canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        canvas.setStyleSheet("background-color: white;")

        # Deleting previous content from the Layout
        if self.parent_widget.layout():
            while self.parent_widget.layout().count():
                item = self.parent_widget.layout().takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
            self.parent_widget.layout().addWidget(canvas)

        # Saving
        self.canvases[key] = canvas
        return fig

    def plot_success_gauge_kpi_from_df(self, df: pd.DataFrame, title_label: QLabel = None, percentage_label: QLabel = None, translator=None):
        if df.empty:
            return

        # Success calculation
        total_steps = int(df['Step Count'].iloc[0])
        error_steps = int(df['Error Steps'].iloc[0])
        success_rate = 100 * (total_steps - error_steps) / total_steps

        # Colors by success rate
        if success_rate < 33:
            percent_color = '#E63946'  # Red
        elif success_rate < 66:
            percent_color = '#F4A261'  # Orange
        else:
            percent_color = '#2A9D8F'  # Green

        # Update the graph title
        if title_label:
            title_label.setText(translator.tr("gauge_title"))
            title_label.setAlignment(Qt.AlignCenter)
            title_label.setStyleSheet("font-weight: bold; font-size: 16px; color: navy; padding-top: 13px;")
            title_label.setFixedHeight(30)

        # Percentage update
        if percentage_label:
            percentage_label.setText(f"{success_rate:.1f}%")
            percentage_label.setAlignment(Qt.AlignCenter)
            percentage_label.setStyleSheet(f"color: {percent_color}; font-weight: bold; font-size: 24px")

        # Creating a canvas
        fig = self.get_or_create_canvas("gauge")
        fig.set_size_inches(5, 3)  # Physical size in relative distances

        ax = fig.add_subplot(111, polar=True)
        ax.set_theta_offset(np.pi)
        ax.set_theta_direction(-1)
        ax.set_axis_off()

        # Color zones
        zones = [
            (0, 0.33 * np.pi, '#E63946'),
            (0.33 * np.pi, 0.66 * np.pi, '#F4A261'),
            (0.66 * np.pi, np.pi, '#2A9D8F')
        ]
        for start, end, color in zones:
            ax.barh(1, end - start, left=start, height=1, color=color, edgecolor='white')

        # Needle
        angle = (success_rate / 100.0) * np.pi
        ax.plot([angle, angle], [0, 0.95], color='black', linewidth=3)

        # Finish drawing
        fig.tight_layout()
        self.canvases["gauge"].draw()

    def plot_variable_over_time_from_df(self, df: pd.DataFrame, variable: str, translator = None):
        if df.empty or variable not in df.columns:
            return

        df = df.sort_values("Test Date")
        x = pd.to_datetime(df['Test Date'])
        y = df[variable]

        fig = self.get_or_create_canvas(variable, figsize=(4.5, 2.8))
        ax = fig.add_subplot(111)

        if variable == "Fall Risk":
            ax.yaxis.set_major_formatter(PercentFormatter(xmax=1.0, decimals=1))

        ax.plot(x.dt.strftime("%d.%m.%y"), y, marker='o')

        translation_keys = {
            "Fall Risk": "graph_title_fall_risk",
            "Step Count": "graph_title_step_count",
            "Error Steps": "graph_title_error_steps"
        }

        key = translation_keys.get(variable, variable)
        if translator:
            translated_title = translator.tr(key)
        else:
            translated_title = variable
        ax.set_title(translated_title, fontsize=10, fontweight='bold', color='navy')

        # ax.set_title(f"{variable} Over Time", fontsize=10, fontweight='bold', color='navy')
        ax.set_ylabel(variable, fontsize=8)
        ax.tick_params(axis='x', labelrotation=45, labelsize=7)
        ax.tick_params(axis='y', labelsize=7)

        fig.tight_layout(pad=1.5)
        self.canvases[variable].draw()

    def clear_plot(self, key: str):
        # Delete previous canvas if it exists
        canvas = self.canvases.get(key)
        if canvas:
            try:
                canvas.setParent(None)
            except RuntimeError:
                pass  # The canvas has probably already been deleted

        self.canvases.pop(key, None)

        # Create an empty figure
        fig = Figure(figsize=(5, 3))
        canvas = FigureCanvas(fig)
        canvas.setStyleSheet("background-color: white;")
        canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout = self.parent_widget.layout()
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
            layout.addWidget(canvas)

        # Saving the new canvas in the dictionary
        self.canvases[key] = canvas

        # Try to draw (only if still exists)
        try:
            canvas.draw()
        except RuntimeError:
            pass

    def clear_all_graphs(self):
        for key in list(self.canvases.keys()):
            self.clear_plot(key)
