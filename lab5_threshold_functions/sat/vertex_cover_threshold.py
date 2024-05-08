from typing import List, Optional

import pycosat

from lab5_threshold_functions.sat.types import VertexSets
from lab5_threshold_functions.utils.dimacs import edgeList

n = 0


# x: variables 1, 2, 3, ..., n
# y: variables n + 1, n + 2, ...
def y(i, j):
    return int(n + (i + j) * (i + j + 1) / 2 + i) + 1


def solve_vertex_cover_threshold(graph: VertexSets, k: int) -> Optional[List[int]]:
    """
    Solve vertex cover problem through reduction to a SAT problem with threshold
    functions and using a SAT solver.

    Denote:
    - V = {v_1, v_2, ..., v_n} (n = |V|)
    - k - number of vertices for cover

    Steps for reduction:
    1. For every vertex v_i create variable x_i for i in [1, n]
    2. For every edge (u, v) add clause (u or v) to the formula (ensures that
       every vertex is covered)
    3. Create variables y_i_j; i in [0, n], j in [0, n]; y_i_j is true, if
       for variables x_1, x_2, ..., x_i at least j are true (false otherwise)
    4. Set y_i_0 for all i to true (ensures cover), y_0_j for j > 0 to false
       (there can be at most 100% true variables)
    5. For every pair (i, j) (1 <= i, j <= n) add implication:
       (y_i-1_j => y_i_j) and ((y_i-1_j-1 and x_i) => y_i_j)
       This can be transformed to CNF form (using a => b <=> -a or b):
       (-y_i-1_j or y_i_j) and (-y_i-1_j-1 or -x_i or y_i_j)
    6. Add clause -y_n_k+1 (ensure that at most k vertices are used)

    :param graph: graph as list of sets of neighbors
    :param k: this many vertices have to cover the graph
    :return: solved vertex cover for given k or None if it's not possible
    """
