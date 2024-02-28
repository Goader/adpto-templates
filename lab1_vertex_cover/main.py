import time
import os

from vertex_cover.brute_force import brute_force
from vertex_cover.types import EdgeList, VertexSets
from utils.dimacs import *

graph_names = [
    "e5",
    "e10",
    "e20",
    "e40",
    "e150",
    "s25",
    "s50",
    "s500",
    "b20",
    "b30",
    "b100",
    "k330_a",
    "k330_b",
    "k330_c",
    "m20",
    "m30",
    "m40",
    "m50",
    "m100",
    "p20",
    "p35",
    "p60",
    "p150",
    "r30_01",
    "r30_05",
    "r50_001",
    "r50_01",
    "r50_05",
    "r100_005",
]


if __name__ == "__main__":
    graph_dir = "graphs"
    solution_dir = "solutions"

    if not os.path.exists(graph_dir):
        raise FileNotFoundError(f"Create {graph_dir} and add graph files")

    if not os.path.exists(solution_dir):
        os.mkdir(solution_dir)

    for name in graph_names:
        graph_filename = os.path.join(graph_dir, name)
        solution_filename = os.path.join(solution_dir, f"{name}.sol")

        G: VertexSets = loadGraph(graph_filename)
        G_edge_list: EdgeList = edgeList(G)

        t0 = time.time()
        print(name)
        for k in range(1, len(G)):
            # TODO: implement kernelization
            # graph_kernel, k, solution = kernelize(...)

            # TODO: implement solutions
            solution = brute_force(..., k)

            if not solution:
                continue

            print("solution k:", len(solution))
            print("VC:", isVC(G_edge_list, solution))
            saveSolution(solution_filename, solution)
            break

        print(f'Elapsed time: {time.time() - t0:.4f}s')
        print()
