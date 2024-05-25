class Node:
    def __init__(self, name):
        self.name = name
        self.adjacents = {}

    def add_adjacent(self, node, weight):
        self.adjacents[node] = weight

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        if name not in self.nodes:
            self.nodes[name] = Node(name)

    def add_edge(self, from_node, to_node, traffic_volume, wait_time, accidents):
        if from_node in self.nodes and to_node in self.nodes:
            weight = self.calculate_combined_weight(traffic_volume, wait_time, accidents)
            self.nodes[from_node].add_adjacent(self.nodes[to_node], weight)

            # Si la arista es de un semáforo a una salida, evalúa la necesidad del semáforo
            if from_node.startswith("S") and to_node.startswith("O"):
                needs_light = self.evaluate_node(from_node)
                self.nodes[from_node].add_adjacent(self.nodes[to_node], 1 if needs_light else 0)

    def calculate_combined_weight(self, traffic_volume, wait_time, accidents):
        weight_traffic_volume = 0.5
        weight_wait_time = 0.3
        weight_accidents = 0.2
        combined_weight = (traffic_volume * weight_traffic_volume +
                           wait_time * weight_wait_time +
                           accidents * weight_accidents)
        return combined_weight

    def evaluate_node(self, node_name):
        if node_name not in self.nodes:
            return False

        weight_threshold = 10  # Ajusta este umbral según sea necesario
        node = self.nodes[node_name]

        for adj_node, weight in node.adjacents.items():
            if weight > weight_threshold:
                return True
        return False

    def needs_traffic_light(self, node_name):
        return self.evaluate_node(node_name)
