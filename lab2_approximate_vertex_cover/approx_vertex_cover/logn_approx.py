from approx_vertex_cover.types import EdgeList


def logn_approx(graph: EdgeList) -> set[int]:
    """
    Approximation algorithm for the Vertex Cover problem, which takes the vertex
    with the highest degree and adds it to the solution.

    Approximation factor: log(n)

    :param graph: graph represented as a list of edges
    :return: set of vertices that approximate the cover
    """
    pass
