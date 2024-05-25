class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def evaluate_intersection(self):
        result = any(self.model.evaluate_node(node_name) for node_name in self.model.nodes if node_name.startswith('S'))
        return "It is advisable to install a traffic light" if result else "No need to install a traffic light"

    def evaluate_node(self, node_name):
        result = self.model.evaluate_node(node_name)
        return result

    def get_graph(self):
        return self.model

    def set_edge_attributes(self, from_node, to_node, traffic_volume, wait_time, accidents):
        self.model.add_edge(from_node, to_node, traffic_volume, wait_time, accidents)
