# APTO Piotr Faliszewski 2018
# Test solution for the VertexCover problem

import os
import os.path


# graphs list
graphs = [
    ("e5"),
    ("e10"),
    ("e20"),
    ("e40"),
    ("e150"),
    ("s25"),
    ("s50"),
    ("s500"),
    ("b20"),
    ("b30"),
    ("b100"),
    ("k330_a"),
    ("k330_b"),
    ("k330_c"),
    ("m20"),
    ("m30"),
    ("m40"),
    ("m50"),
    ("m100"),
    ("p20"),
    ("p35"),
    ("p60"),
    ("p150"),
    ("r30_01"),
    ("r30_05"),
    ("r50_001"),
    ("r50_01"),
    ("r50_05"),
    ("r100_005"),
]


from utils.dimacs import *
from sys import *


def loadSolution(name):
    f = open(name, "r")
    s = f.readline().strip()
    C = s.split(",")
    C = [int(c) for c in C]
    return C


if len(argv) > 1:
    print("Invocation:")
    print("  python grademe.py")
    print("")
    print("Looks for graphs in the directory:")
    print("  graphs_solutions")
    print("Solutions should have name:")
    print("  <name>.sol")
    exit()


curr_dir = os.path.dirname(os.getcwd())
graph_dir = os.path.join(curr_dir, "graphs")
solution_dir = os.path.join(curr_dir, "graphs_solutions")


def checkGraph(name):
    s = name + "\t :  "
    size = 99999
    try:
        graph_name = os.path.join(graph_dir, name)
        G = loadGraph(graph_name)
        size = len(G)
        solution_name = os.path.join(solution_dir, name + ".sol")
        C = loadSolution(solution_name)
    except IOError:
        s += "--- (%d)" % size
        return (s, size, False)

    E = edgeList(G)
    if isVC(E, C):
        s += "OK  (VC = %d)" % len(C)
        return (s, len(C), True)
    else:
        s += "FAIL! (99999)"
        return (s, 99999, False)


score = 0
total = 0
output = ""


for name in graphs:
    (s, size, ans) = checkGraph(name)
    total += size
    if ans:
        score += 1
    print(s)
    output += str(size) + ","

print("")
print("SOLVED = %d/%d" % (score, len(graphs)))
print("TOTAL  = %d" % total)

print("")
print('=split("%d,%d,%s",",")' % (score, total, output))
