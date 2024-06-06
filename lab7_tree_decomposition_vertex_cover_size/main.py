import os

from vertex_cover.vertex_cover_size import vertex_cover_size
from vertex_cover.types import EdgeList, VertexSets, TreeDecomposition
from utils.dimacs import *

graph_names = [
    "e5",
    "e10",
    "e20",
    "b20",
    "k330_a",
    "m20",
    "p60",
]


if __name__ == "__main__":
    graph_dir = "graphs"
    solution_dir = "solutions"
    for name in graph_names:
        graph_filename = os.path.join(graph_dir, f"{name}.gr")
        tree_decomposition_filename = os.path.join(graph_dir, f"{name}.tw")
        solution_filename = os.path.join(solution_dir, f"{name}.sol")

        G: VertexSets = loadGRGraph(graph_filename)
        G_edge_list: EdgeList = edgeList(G)
        tree_decomp: TreeDecomposition = loadDecomposition(tree_decomposition_filename)

        k = vertex_cover_size(G, tree_decomp)
        print(name)
        print("solution k:", k)
        print()
