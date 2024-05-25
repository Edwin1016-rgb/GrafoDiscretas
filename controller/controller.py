class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def evaluate_intersection(self):
        result = self.model.evaluate_graph()
        return "It is advisable to install a traffic light" if result else "No need to install a traffic light"

    def evaluate_node(self, node_name):
        result = self.model.evaluate_node(node_name)
        return result

    def get_graph(self):
        return self.model

    def set_edge_attributes(self, from_node, to_node, traffic_volume, wait_time, accidents):
        self.model.add_edge(from_node, to_node, traffic_volume, wait_time, accidents)
