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

# TODO: add graphs for coloring
coloring_names = []


def check_coloring(solution) -> bool:
    # TODO: implement coloring solution check
    pass


if __name__ == "__main__":
    calculate_SAT_probabilities_and_plot()

    # X3C -> SAT
    """
    x3c_dir = "graphs_x3c"
    for name in x3c_names:
        x3c_filename = os.path.join(x3c_dir, name)
        n, sets = loadX3C(x3c_filename)

        satisfiable = True if name.split(".")[1] == "yes" else False

        print(name)
        result = solve_x3c(n, sets)
        print(f"result: {result}, truth: {satisfiable}")
        print()
    """

    # graph coloring -> SAT
    """
    coloring_dir = "graphs_coloring"
    for name in coloring_names:
        graph_filename = os.path.join(coloring_dir, name)

        G: VertexSets = loadGraph(graph_filename)
        G_edge_list: EdgeList = edgeList(G)

        print(name)
        for k in range(1, len(G)):
            solution = solve_coloring(G_edge_list, k)
            
            if not solution:
                continue
            
            if not check_coloring(solution):
                continue

            print("solution k:", k)
            print()
            break
    """
