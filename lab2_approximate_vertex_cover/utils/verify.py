# APTO Piotr Faliszewski 2018
# Test solution for the VertexCover problem


from utils.dimacs import *
from sys import *


def loadSolution(name):
    f = open(name, "r")
    s = f.readline().strip()
    C = s.split(",")
    C = [int(c) for c in C]
    return C


if len(argv) < 3:
    print("Invocation:")
    print("  python verify.py graphs-file solution-file")
    exit()

try:
    G = loadGraph(argv[1])
    C = loadSolution(argv[2])
except IOError:
    print("IOError")

E = edgeList(G)
if isVC(E, C):
    print("OK", len(C))
else:
    print("Fail!")
