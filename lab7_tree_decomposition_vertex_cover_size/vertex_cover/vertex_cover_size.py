import math
from itertools import combinations
from typing import Iterable, Set

from .types import (
    VertexSets,
    TreeDecomposition,
)

from utils.dimacs import isVC


def check_subgraph_VC(
    graph: VertexSets, vertices_subset: Iterable[int], candidate_vertices: Iterable[int]
) -> bool:
    """
    Answers the question: if for given graph we check the subgraph given by the
    vertices subset, does the set of candidate vertices create a Vertex Cover
    for this subgraph?

    :param graph: graphs represented as a list of sets (incident vertices)
    :param vertices_subset: vertices of subgraph
    :param candidate_vertices: candidate solution for Vertex Cover
    :returns: whether candidate vertices are a Vertex Cover solution for subgraph
    """
    edges = set()
    for vertex in vertices_subset:
        for neighbor in graph[vertex]:
            u = min(vertex, neighbor)
            v = max(vertex, neighbor)
            edges.add((u, v))

    return isVC(list(edges), candidate_vertices)


# map set of vertices (C) to its size (or infinity if it's not VC)
memoization_table = {}


def f(graph: VertexSets, bags: TreeDecomposition, bag_idx: int, C: Set[int]) -> int:
    # check memoization table, update if we don't have Vertex Cover
    global memoization_table

    # your code here


def vertex_cover_size(graph: VertexSets, tree_decomp: TreeDecomposition) -> int:
    """
    Calculates size of minimal Vertex Cover for given graph, using its tree
    decomposition.

    :param graph: graphs represented as a list of sets (incident vertices)
    :param tree_decomp: tree decomposition of graph
    :returns: size of minimal Vertex Cover
    """
    best_k = math.inf

    # decomposition tree root vertices
    bag = tree_decomp[1].bag

    # check all combinations of all sizes, choose best (smallest) vertex cover size
    for size in range(len(bag) + 1):
        for C in combinations(bag, size):
            k = f(graph, tree_decomp, 1, set(C))

            if k < best_k:
                best_k = k

    return best_k
