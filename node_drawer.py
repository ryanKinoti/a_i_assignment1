import os
import networkx as nx
from matplotlib import pyplot as plt

path = 'answers'
os.makedirs(path, exist_ok=True)


def graph_drawer(nodes, nodes_with_edges, path_to_file):
    """declaring necessary libraries and placing nodes and edges"""
    graph = nx.Graph()
    graph.add_nodes_from(nodes)
    graph.add_weighted_edges_from(nodes_with_edges)

    pos = nx.spring_layout(graph, k=5.00)
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=10, font_color='black')
    nx.draw_networkx_edge_labels(graph, pos,
                                 edge_labels={(u, v): str(d['weight']) for u, v, d in graph.edges(data=True)})
    # plt.show()
    plt.savefig(path_to_file, bbox_inches='tight', dpi=400)
    plt.close()
