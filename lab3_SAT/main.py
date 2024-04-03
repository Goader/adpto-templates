import time
import os

from sat.x3c import solve_x3c
from sat.coloring import solve_coloring
from sat.satisfiability import calculate_SAT_probabilities_and_plot
from sat.types import VertexSets, EdgeList
from utils.dimacs import *

x3c_names = [
    "10.no.x3c",
    "10.yes.x3c",
    "50.no.x3c",
    "50.yes.x3c",
    "100.no.x3c",
    "200.no.x3c",
    "200.yes.x3c",
    "350.no.x3c",
    "350.yes.x3c",
    "500.no.x3c",
    "500.yes.x3c",
    "600.no.x3c",
    "600.yes.x3c",
]

coloring_names = [
    '1-FullIns_3.col',
    '1-FullIns_4.col',
    '1-FullIns_5.col',
    'DSJC125.1.col',
    'le450_5a.col',
    'le450_5b.col',
    'mug88_1.col',
    'queen5_5.col',
    'queen6_6.col',
    'queen7_7.col',
]


def check_coloring(G_edge_list, solution) -> bool:
    def from_idx(idx):
        idx = idx - 1
        color = idx % k
        vertex = idx // k
        return vertex, color

    vertex2color = dict()
    for idx in solution:
        if idx < 0:
            continue

        vertex, color = from_idx(idx)
        if vertex in vertex2color:
            return False
        vertex2color[vertex] = color

    for edge in G_edge_list:
        v1, v2 = edge
        if v1 not in vertex2color or v2 not in vertex2color:
            return False
        if vertex2color[v1] == vertex2color[v2]:
            return False

    return True


if __name__ == "__main__":
    calculate_SAT_probabilities_and_plot()

    # X3C -> SAT
    # x3c_dir = "graphs_x3c"
    # for name in x3c_names:
    #     x3c_filename = os.path.join(x3c_dir, name)
    #     n, sets = loadX3C(x3c_filename)
    #
    #     satisfiable = True if name.split(".")[1] == "yes" else False
    #
    #     print(name)
    #     result = solve_x3c(n, sets)
    #     print(f"result: {result}, truth: {satisfiable}")
    #     print()

    # graph coloring -> SAT
    # coloring_dir = "graphs_coloring"
    # for name in coloring_names:
    #     graph_filename = os.path.join(coloring_dir, name)
    #
    #     G: VertexSets = loadGraph(graph_filename)
    #     G_edge_list: EdgeList = edgeList(G)
    #
    #     print(name)
    #     t0 = time.time()
    #     for k in range(1, len(G)):
    #         solution = solve_coloring(G_edge_list, k)
    #
    #         if not solution:
    #             continue
    #
    #         if not check_coloring(G_edge_list, solution):
    #             continue
    #
    #         print("solution k:", k)
    #         print(f'elapsed time: {time.time() - t0:.4f}s')
    #         print()
    #         break
