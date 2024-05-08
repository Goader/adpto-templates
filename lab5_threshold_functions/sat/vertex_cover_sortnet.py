from typing import List, Optional

import pycosat

from lab5_threshold_functions.sat.types import VertexSets
from lab5_threshold_functions.utils.dimacs import edgeList


class SortNet:
    def __init__(self, start: int, lines: List[int], generate_equivalences: bool):
        # first available variable
        self.start = start

        # current variable ready to be used
        self.current = start

        # current variables for the input lines
        self.lines = lines.copy()

        # if True, generate equivalences in addition to implications in comparators
        self.generate_equivalences = generate_equivalences

        # current SAT formula
        self.formula = []

    def compare_lines(self, i: int, j: int):
        """
        Compares i-th and j-th lines, higher values go to the earlier line (with
        lower index).
        """


def insertion_sort_formula(a: int, b: int, k: int) -> List[List[int]]:
    """
    Uses sorting network with insertion sort to generate CNF formula for given
    variables.
    """


def solve_vertex_cover_sortnet(graph: VertexSets, k: int) -> Optional[List[int]]:
    """
    Solve vertex cover problem through reduction to a SAT problem with sorting
    network and using a SAT solver.

    Denote:
    - V = {v_1, v_2, ..., v_n} (n = |V|)
    - k - number of vertices for cover

    Steps for reduction:
    1. For every vertex v_i create variable x_i for i in [1, n]
    2. For every edge (u, v) add clause (u or v) to the formula (ensures that
       every vertex is covered)
    3. Use sorting network to ensure that at most k variables are true

    :param graph: graph as list of sets of neighbors
    :param k: this many vertices have to cover the graph
    :return: solved vertex cover for given k or None if it's not possible
    """
