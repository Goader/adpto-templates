import os
from time import time

from ilp.approx_vertex_cover import approx_vertex_cover_solver
from ilp.example import solve_and_print_example
from ilp.vertex_cover import vertex_cover_solver
from ilp.weighted_vertex_cover import weighted_vertex_cover_solver

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


def calculate_vertex_cover():
    graph_dir = "graphs"
    solution_dir = "solutions"
    for name in graph_names:
        graph_filename = os.path.join(graph_dir, name)
        solution_filename = os.path.join(solution_dir, f"{name}.sol")
        G = loadGraph(graph_filename)
        G_edge_list = edgeList(G)

        print(name)
        solution = vertex_cover_solver(G)
        if not solution:
            print("solution not found")
            continue

        solution, k = solution

        print("solution k:", k)
        print("VC:", isVC(G_edge_list, solution))
        print()
        saveSolution(solution_filename, solution)


def calculate_weighted_vertex_cover():
    graph_dir = "graphs"
    for name in graph_names:
        graph_filename = os.path.join(graph_dir, name)
        G = loadGraph(graph_filename)
        G_edge_list = edgeList(G)

        print(name)
        try:
            sol_0, k_0, cost_0 = weighted_vertex_cover_solver(G, 0)
            sol_0_5, k_0_5, cost_0_5 = weighted_vertex_cover_solver(G, 0.5)
            sol_1, k_1, cost_1 = weighted_vertex_cover_solver(G, 1)
        except Exception:
            print("solution not found")
            continue

        print("solution k_0:", k_0)
        print("cost 0", cost_0)
        print("VC:", isVC(G_edge_list, sol_0))

        print("solution k_0:", k_0_5)
        print("cost 0_5", cost_0_5)
        print("VC:", isVC(G_edge_list, sol_0_5))

        print("solution k_0:", k_1)
        print("cost 1", cost_1)
        print("VC:", isVC(G_edge_list, sol_1))
        print()


def calculate_approx_vertex_cover():
    graph_dir = "graphs"
    solution_dir = "solutions"
    for name in graph_names:
        graph_filename = os.path.join(graph_dir, name)
        G = loadGraph(graph_filename)
        G_edge_list = edgeList(G)

        print(name)
        try:
            time_exact = time()
            sol_exact, k_exact = vertex_cover_solver(G)
            time_exact = round(time() - time_exact, 5)
        except Exception:
            print("exact solution not found")
            continue

        try:
            time_approx = time()
            sol_approx, k_approx = approx_vertex_cover_solver(G)
            time_approx = round(time() - time_approx, 5)
        except Exception:
            print("approximate solution not found")
            k_approx = "-"
            time_approx = None
            sol_approx = None

        print("exact k:", k_exact)
        print("approximate k:", k_approx)
        print("exact time:", time_exact)
        print("approx time:", time_approx)
        print("VC exact:", isVC(G_edge_list, sol_exact))
        print("VC approx:", isVC(G_edge_list, sol_approx))
        print()


if __name__ == "__main__":
    # solve_and_print_example()
    calculate_vertex_cover()
    # calculate_weighted_vertex_cover()
    # calculate_approx_vertex_cover()
