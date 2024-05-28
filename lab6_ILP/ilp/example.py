from pulp import *


def solve_and_print_example():
    """
    Example ILP problem solved with PuLP and default CBC solver.
    Problem:
    Minimize x + y (first integers, then real numbers) with constraints:
    y >= x - 1
    y >= -4x + 4
    y <= -0.5x + 3
    """
