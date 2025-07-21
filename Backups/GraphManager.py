import numpy as np
import pandas as pd
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.ticker import PercentFormatter
from DatabaseUtils import get_latest_test_data, get_patient_tests

class GraphManager:
    def __init__(self, parent_widget: QWidget):
        self.parent_widget = parent_widget
        self.layout = parent_widget.layout() or QGridLayout()
        if parent_widget.layout() is None:
            parent_widget.setLayout(self.layout)
        self.canvases = {}

    def get_or_create_canvas(self, key: str, figsize=(5, 3)) -> Figure:
        if key in self.canvases:
            # מחיקת קנבס קודם
            canvas = self.canvases[key]
            fig = Figure(figsize=figsize)
            if canvas:
                canvas.setParent(None)
                del self.canvases[key]

        # יצירת פיגורה חדשה
        fig = Figure(figsize=(5, 3))
        canvas = FigureCanvas(fig)

        # לוודא שהקנבס תופס את כל המרחב
        canvas.setMinimumSize(self.parent_widget.width(), self.parent_widget.height())
        canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        canvas.setStyleSheet("background-color: white;")

        # מחיקת תוכן קודם מה־Layout
        if self.parent_widget.layout():
            while self.parent_widget.layout().count():
                item = self.parent_widget.layout().takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
            self.parent_widget.layout().addWidget(canvas)

        # שמירה
        self.canvases[key] = canvas
        return fig

    # def plot_success_gauge_kpi(self, patient_id: int, title_label: QLabel = None, percentage_label: QLabel = None):
    #     df = get_latest_test_data(patient_id)
    #     if df.empty:
    #         return
    #
    #     total_steps = int(df['Step Count'].iloc[0])
    #     error_steps = int(df['Error Steps'].iloc[0])
    #     success_rate = 100 * (total_steps - error_steps) / total_steps
    #
    #     if success_rate < 33:
    #         percent_color = '#E63946'
    #     elif success_rate < 66:
    #         percent_color = '#F4A261'
    #     else:
    #         percent_color = '#2A9D8F'
    #
    #     if title_label:
    #         title_label.setText("KPI – Successful Steps / Total Steps")
    #         title_label.setStyleSheet("font-weight: bold; font-size: 16px; color: navy; padding-top: 13px;")
    #         title_label.setFixedHeight(30)
    #
    #     if percentage_label:
    #         percentage_label.setText(f"{success_rate:.1f}%")
    #         percentage_label.setStyleSheet(f"color: {percent_color}; font-weight: bold; font-size: 24px")
    #
    #     fig = self.get_or_create_canvas("gauge")
    #     ax = fig.add_subplot(111, polar=True)
    #     ax.set_theta_offset(np.pi)
    #     ax.set_theta_direction(-1)
    #     ax.set_axis_off()
    #
    #     zones = [
    #         (0, 0.33 * np.pi, '#E63946'),
    #         (0.33 * np.pi, 0.66 * np.pi, '#F4A261'),
    #         (0.66 * np.pi, np.pi, '#2A9D8F')
    #     ]
    #     for start, end, color in zones:
    #         ax.barh(1, end - start, left=start, height=1, color=color, edgecolor='white')
    #
    #     angle = (success_rate / 100.0) * np.pi
    #     ax.plot([angle, angle], [0, 0.95], color='black', linewidth=3)
    #
    #     fig.tight_layout()
    #     self.canvases["gauge"].draw()
    #
    # def plot_variable_over_time(self, patient_id: int, variable: str):
    #     df = get_patient_tests(patient_id)
    #     if df.empty or variable not in df.columns:
    #         return
    #
    #     df = df.sort_values("Test Date")
    #     x = pd.to_datetime(df['Test Date'])
    #     y = df[variable]
    #
    #     fig = self.get_or_create_canvas(variable, figsize=(4.5, 2.8))
    #     ax = fig.add_subplot(111)
    #
    #     if variable == "Fall Risk":
    #         ax.yaxis.set_major_formatter(PercentFormatter(xmax=1.0, decimals=1))
    #
    #     ax.plot(x.dt.strftime("%d.%m.%y"), y, marker='o')
    #
    #     ax.set_title(f"{variable} Over Time", fontsize=10, fontweight='bold', color='navy')
    #     # ax.set_xlabel("Test Date", fontsize=8)
    #     ax.set_ylabel(variable, fontsize=8)
    #     ax.tick_params(axis='x', labelrotation=45, labelsize=7)
    #     ax.tick_params(axis='y', labelsize=7)
    #
    #     fig.tight_layout(pad=1.5)
    #     self.canvases[variable].draw()

    def plot_success_gauge_kpi_from_df(self, df: pd.DataFrame,
                                       title_label: QLabel = None,
                                       percentage_label: QLabel = None,
                                       translator = None):
        if df.empty:
            return

        total_steps = int(df['Step Count'].iloc[-0])
        error_steps = int(df['Error Steps'].iloc[-0])
        success_rate = 100 * (total_steps - error_steps) / total_steps

        if success_rate < 33:
            percent_color = '#E63946'
        elif success_rate < 66:
            percent_color = '#F4A261'
        else:
            percent_color = '#2A9D8F'

        if title_label:
            title_label.setText(translator.tr("gauge_title"))
            title_label.setStyleSheet("font-weight: bold; font-size: 16px; color: navy; padding-top: 13px;")
            title_label.setFixedHeight(30)

        if percentage_label:
            percentage_label.setText(f"{success_rate:.1f}%")
            percentage_label.setStyleSheet(f"color: {percent_color}; font-weight: bold; font-size: 24px")

        fig = self.get_or_create_canvas("gauge")
        ax = fig.add_subplot(111, polar=True)
        ax.set_theta_offset(np.pi)
        ax.set_theta_direction(-1)
        ax.set_axis_off()

        zones = [
            (0, 0.33 * np.pi, '#E63946'),
            (0.33 * np.pi, 0.66 * np.pi, '#F4A261'),
            (0.66 * np.pi, np.pi, '#2A9D8F')
        ]
        for start, end, color in zones:
            ax.barh(1, end - start, left=start, height=1, color=color, edgecolor='white')

        angle = (success_rate / 100.0) * np.pi
        ax.plot([angle, angle], [0, 0.95], color='black', linewidth=3)

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
