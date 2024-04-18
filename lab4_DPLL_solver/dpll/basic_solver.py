from typing import Dict, List, Optional, Tuple, Union


_recurrence_counter = 0


def _simplify_clause(clause: List[int], values: Dict[int, int]) -> Optional[List[int]]:
    """
    Simplifies a single SAT formula clause (an alternative of variables), i.e.
    removes False variables and returns satisfied formula if any variable is True.

    For clauses we assume that:
    - None clause is satisfied (since it's a lack of clause)
    - [] clause is not satisfied (since it's an empty alternative, similar to
      sum of zeroes being zero)

    :param clause: clause, list of integers representing variables
    :param values: values of variables
    :return: one of:
    - None if clause is satisfied
    - simplified clause otherwise
    """


def _simplify_formula(
    formula: List[List[int]], values: Dict[int, int]
) -> Optional[List[List[int]]]:
    """
    Simplifies a SAT formula, i.e. simplifies each clause in the formula.

    For formulas we assume that:
    - None formula is not satisfied
    - [] formula is satisfied (since it's an empty conjunction, similar to
      product of ones being one)

    :param formula: list of clauses in CNF form
    :param values: values of variables
    :return: simplified formula
    """


def _solve(
    formula: List[List[int]], values: Dict[int, int]
) -> Union[Dict[int, int], str]:
    """
    Helper function for DPLL solver.

    For clauses we assume that:
    - None clause is satisfied (since it's a lack of clause)
    - [] clause is not satisfied (since it's an empty alternative, similar to
      sum of zeroes being zero)

    For formulas we assume that:
    - None formula is not satisfied
    - [] formula is satisfied (since it's an empty conjunction, similar to
      product of ones being one)

    :param formula: list of clauses in CNF form
    :param values: dictionary of values of clause variables, mapping variable
    number (starting from 1) to either -1 (False) or 1 (True)
    :return: values
    """
    global _recurrence_counter
    _recurrence_counter += 1

    raise NotImplementedError("Implement me!")


def basic_dpll_solve(
    formula: List[List[int]],
) -> Tuple[Union[Dict[int, int], str], int]:
    """
    Basic DPLL (Davis, Putnam, Logemann, Loveland) solver implementation for
    checking SAT formulas satisfiability.

    :param formula: list of clauses in CNF form
    :returns: tuple of:
    - list of values if formula is satisfiable, "UNSAT" otherwise
    - number of recurrent calls to the solver procedure
    """
    global _recurrence_counter
    _recurrence_counter = 0

    result = _solve(formula, values=dict())
    return result, _recurrence_counter
