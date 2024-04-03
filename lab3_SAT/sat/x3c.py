import pycosat

from sat.types import ThreeSets


def solve_x3c(n: int, sets: ThreeSets) -> bool:
    """
    Solve Exact 3-set Cover (X3C) problem through reduction to a SAT problem
    and using a SAT solver.

    Denote:
    - N = {1, 2, ..., 3k}, n = |N|
    - *S = {S1, S2, ..., Sm}, where |Si| = 3 and m <= 3k

    Steps for reduction:
    1. For every element N_j create variable x_j for j in [1, n]
    2. For every variable add clause with sets containing this variable, e.g.:
       (Sa or Sb or Sc); there can be 1, 2 or 3 such sets (ensures that at
       least one set is chosen)
    3. For every variable add exclusivity clauses (makes sure that at most one
       set is chosen, e.g. (~Sa or ~Sb) and (~Sb or ~Sc) and (~Sa or ~Sc)

    :param n: number of variables, it has to be a multiple of 3
    :param sets: list of sets with variables, where each set has exactly 3
    elements and each variable is contained in at most 3 sets
    :return: whether k sets (n // 3) can be selected such that each element
    is contained in exactly one of those sets
    """
    pass
