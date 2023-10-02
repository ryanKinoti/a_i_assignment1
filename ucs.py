import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue


class UCS:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal

    def search(self):
        visited = set()
        queue = PriorityQueue()
        queue.put((0, self.start, [self.start]))  # Priority, vertex, path

        while queue:
            cost, current, path = queue.get()
            if current == self.goal:
                return path  # Return the successful path
            if current in visited:
                continue
            visited.add(current)
            for neighbor, data in self.graph[current].items():
                if neighbor not in visited:
                    total_cost = cost + data['weight']
                    queue.put((total_cost, neighbor, path + [neighbor]))
        return []  # Return an empty list if no path is found


def ucs_drawer(nodes, nodes_with_edges, start, goal, path_to_file):
    # adding the nodes and their respective edges to the graph
    graph = nx.Graph()
    graph.add_nodes_from(nodes)
    graph.add_weighted_edges_from(nodes_with_edges)

    # implementing the UCS
    ucs = UCS(graph, start, goal)
    path = ucs.search()

    pos = nx.spring_layout(graph, k=0.15)
    nx.draw(graph, pos, with_labels=True, node_color=['red' if node in path else 'skyblue' for node in graph.nodes],
            node_size=2000, font_size=10, font_color='black')
    nx.draw_networkx_edge_labels(graph, pos,
                                 edge_labels={(u, v): str(d['weight']) for u, v, d in graph.edges(data=True)})
    plt.savefig(path_to_file, bbox_inches='tight', dpi=300)
    # plt.show()
