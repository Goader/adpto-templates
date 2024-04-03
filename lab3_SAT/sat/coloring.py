from typing import Optional, List

import pycosat

from sat.types import EdgeList


def solve_coloring(graph: EdgeList, k: int) -> Optional[List[int]]:
    """
    Czy da się przypisać każdemu z wierzchołków jeden z k kolorów tak,
    żeby żadne dwa wierzchołki połączone krawędzią nie miały tego samego koloru.

    Solve Graph Coloring / Vertex Coloring problem through reduction to a SAT
    problem and using a SAT solver.

    Denote:
    - G = (V, E)
    - V = {v_1, v_2, ..., v_n}, |V|
    - colors {1, ..., k}

    Steps for reduction:
    1. For every vertex v_i and color j create variable (v_i,j), taking value
       True if that vertex has color j or False otherwise.
    2. For every vertex v_i create a series of clauses, making sure that it has
       exactly one color:
       (v_i,1 or v_i,2 or ... or v_i,k) and (~x_i,1 or ~x_i,2) and ... and (~x_i,k-1 or ~x_i,k)
    3. For each edge (v_i, v_t) and for each color j create a clause, making sure
       that connected vertices do not have the same color:
       (~x_i,j or ~x_t,j)

    :param graph: graph represented as a list of edges
    :param k: number of colors
    :return: empty list if the graph cannot be colored with k colors, otherwise
    a list returned by the SAT solver, where each element is a variable
    """

    def to_idx(vertex, color):
        """Assuming that vertices are counted from 0"""
        return vertex * k + color + 1

    pass
