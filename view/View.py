import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class View:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Traffic Light Evaluation")

        self.label = tk.Label(root, text="Intersection Evaluation")
        self.label.pack()

        self.evaluate_button = tk.Button(root, text="Evaluate Intersection", command=self.evaluate_intersection)
        self.evaluate_button.pack()

        self.show_graph_button = tk.Button(root, text="Show Graph", command=self.show_graph)
        self.show_graph_button.pack()

        self.evaluate_node_button = tk.Button(root, text="Evaluate Specific Node", command=self.evaluate_node)
        self.evaluate_node_button.pack()

        self.weight_button = tk.Button(root, text="Set Edge Attributes", command=self.set_edge_attributes)
        self.weight_button.pack()

        self.canvas = None

    def evaluate_intersection(self):
        result = self.controller.evaluate_intersection()
        messagebox.showinfo("Result", result)

    def evaluate_node(self):
        node_name = input("Enter node name to evaluate: ")
        result = self.controller.evaluate_node(node_name)
        messagebox.showinfo("Result", f"It is advisable to install a traffic light at {node_name}" if result else f"No need to install a traffic light at {node_name}")

    def show_graph(self):
        graph = self.controller.get_graph()
        self.plot_graph(graph)

    def plot_graph(self, graph):
        G = nx.DiGraph()

        for node_name, node in graph.nodes.items():
            G.add_node(node_name)
            for adj, weight in node.adjacents.items():
                G.add_edge(node_name, adj.name, weight=weight)

        pos = nx.spring_layout(G)
        fig, ax = plt.subplots()

        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        nx.draw(G, pos, with_labels=True, node_color='lightblue', ax=ax, node_size=3000, font_size=10)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)

        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    def set_edge_attributes(self):
        from_node = input("Enter from node: ")
        to_node = input("Enter to node: ")
        traffic_volume = int(input("Enter traffic volume: "))
        wait_time = int(input("Enter wait time (in minutes): "))
        accidents = int(input("Enter number of accidents: "))
        self.controller.set_edge_attributes(from_node, to_node, traffic_volume, wait_time, accidents)