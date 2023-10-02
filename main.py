from node_drawer import *
from ucs import *


def main():
    nodes = [
        'sports_complex', 'siwaka', 'ph1A', 'ph1B', 'phase_2',
        'stc', 'j1', 'mada', 'phase_3', 'parking_lot'
    ]
    nodes_with_edges = [
        ('sports_complex', 'siwaka', 450),
        ('siwaka', 'ph1A', 10), ('siwaka', 'ph1B', 230),
        ('ph1A', 'ph1B', 100), ('ph1A', 'mada', 850),
        ('ph1B', 'stc', 50), ('ph1B', 'phase_2', 112),
        ('stc', 'phase_2', 50), ('stc', 'parking_lot', 250),
        ('phase_2', 'j1', 600), ('phase_2', 'phase_3', 500),
        ('j1', 'mada', 200),
        ('mada', 'parking_lot', 700),
        ('phase_3', 'parking_lot', 350)
    ]

    # file locations
    question_1 = 'answers/question_1.png'
    question_2 = 'answers/question_2.png'

    graph_drawer(nodes, nodes_with_edges, question_1)
    ucs_drawer(nodes, nodes_with_edges, 'sports_complex', 'parking_lot', question_2)


if __name__ == "__main__":
    main()
