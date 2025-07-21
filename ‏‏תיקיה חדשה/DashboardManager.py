# from PySide6.QtWidgets import QGridLayout, QWidget, QVBoxLayout
#
# class DashboardManager:
#     def __init__(self, container_widget: QWidget, graph_manager_factory):
#         """
#         :param container_widget: QWidget that contains the dashboard layout
#         :param graph_manager_factory: Function that creates a new GraphManager instance (e.g. lambda: GraphManager(QWidget))
#         """
#         self.container_widget = container_widget
#         self.layout = container_widget.layout()
#         if not isinstance(self.layout, QGridLayout):
#             raise ValueError("DashboardManager requires a QGridLayout on the container_widget")
#
#         self.graph_manager_factory = graph_manager_factory
#         self.row_count = 0
#         self.column_count = 0
#         self.max_columns = 3  # Default, can be changed
#
#     # Clears the dashboard of all current graphs, including resetting the count
#     def clear_dashboard(self):
#         while self.layout.count():
#             item = self.layout.takeAt(0)
#             widget = item.widget()
#             if widget:
#                 widget.setParent(None)
#         self.row_count = 0
#         self.column_count = 0
#
#     def add_graph(self, plot_function, *args, **kwargs):
#         """
#         Adds a graph to the dashboard.
#         :param plot_function: A function from GraphManager that draws a graph (e.g. gm.plot_fall_risk)
#         :param args: Parameters for the graph
#         :param kwargs: Parameters for the graph
#         """
#         # Create a new graph in a temporary widget
#         wrapper = QWidget()
#         wrapper.setFixedSize(300, 250)  # ⬅️ כאן אתה שולט על הגודל האחיד
#
#         wrapper_layout = QVBoxLayout(wrapper)
#         wrapper.setLayout(wrapper_layout)
#
#         graph_manager = self.graph_manager_factory(wrapper)
#         plot_function(graph_manager, *args, **kwargs)
#
#         for canvas in graph_manager.canvases:
#             wrapper_layout.addWidget(canvas)
#
#         self.layout.addWidget(wrapper, self.row_count, self.column_count)
#
#         self.column_count += 1
#         if self.column_count >= self.max_columns:
#             self.column_count = 0
#             self.row_count += 1
