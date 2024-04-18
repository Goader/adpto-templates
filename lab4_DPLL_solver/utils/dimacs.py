# APTO Piotr Faliszewski 2018
# Load graph in the DIMACS ascii format


def loadGraph(name):
    """Load a graph in the DIMACS ascii format from
       the file "name" and return it as a list of sets"""

    V = 0
    E = 0
    G = []

    f = open(name, "r")
    lines = f.readlines()
    for l in lines:
        s = l.split()
        if len(s) < 1:
            continue
        if s[0] == "c":
            continue
        elif s[0] == "p":
            V = int(s[2]) + 1
            E = int(s[3])
            G = [set() for x in range(V)]
        elif s[0] == "e":
            (x, y) = (int(s[1]), int(s[2]))
            G[x].add(y)
            G[y].add(x)

    f.close()
    return G


def loadGRGraph(name):
    """Load a graph in the DIMACS GR ascii format from
       the PACE-2016 competition"""

    V = 0
    E = 0
    G = []

    f = open(name, "r")
    lines = f.readlines()
    for l in lines:
        s = l.split()
        if len(s) < 1:
            continue
        if s[0] == "c":
            continue
        elif s[0] == "p":
            V = int(s[2]) + 1
            E = int(s[3])
            G = [set() for x in range(V)]
        else:
            (x, y) = (int(s[0]), int(s[1]))
            G[x].add(y)
            G[y].add(x)

    f.close()
    return G


class Bag:
    def __init__(self, id):
        self.id = id
        self.parent = None
        self.children = set()
        self.bag = None


def setParents(Bags, id):
    """set parents in the bags"""
    for ch in Bags[id].children:
        Bags[ch].parent = id
        Bags[ch].children.remove(id)
        setParents(Bags, Bags[ch].id)


def loadDecomposition(name):
    """Load a tree decomposition in the PACE-2016 format"""

    B = 0  # number of bags
    TW = 0
    Bags = []

    f = open(name, "r")
    lines = f.readlines()
    for l in lines:
        s = l.split()
        if len(s) < 1:
            continue
        if s[0] == "c":
            continue
        elif s[0] == "s":
            B = int(s[2])
            TW = int(s[3])
            Bags = [Bag(x) for x in range(B + 1)]
        elif s[0] == "b":
            b = int(s[1])
            l = set([int(x) for x in s[2:]])
            Bags[b].bag = l
        else:
            (x, y) = (int(s[0]), int(s[1]))
            Bags[x].children.add(y)
            Bags[y].children.add(x)

    f.close()
    setParents(Bags, 1)

    return Bags


def saveGraph(name, G, comment):
    """save graph G (list-of-sets) to file "name" in DIMACS ascii format, with comment "comment" """

    E = edgeList(G)
    f = open(name, "w")
    f.write("c %s\n" % comment)
    f.write("p edge %d %d\n" % (len(G), len(E)))

    for (x, y) in E:
        f.write("e %d %d\n" % (x, y))


def loadX3C(name):
    """Load an X3C instance in the format:
       n elements
       s set1
       s set2
       ...
       s last set

       Return a pair (elements, list of sets) where each set is a list and the set at index 0 is a dummy empty set"""

    n = 0
    sets = []

    f = open(name, "r")
    lines = f.readlines()
    for l in lines:
        s = l.split()
        if len(s) < 1:
            continue
        if s[0] == "c":
            continue
        elif s[0] == "n":
            n = int(s[1])
        elif s[0] == "s":
            (x, y, z) = (int(s[1]), int(s[2]), int(s[3]))
            sets += [[x, y, z]]

    f.close()
    return (n, sets)


def edgeList(G):
    """convert list-of-sets graph representation to a list of edges"""
    V = len(G)
    E = []
    for v in range(V):
        for u in G[v]:
            if v < u:
                E += [(v, u)]
    return E


def isVC(E, C):
    """checks if C is a vertex cover for graph E
       C -- set of vertices
       E -- graph represented as a list of edges
       returns True/False"""
    for (x, y) in E:
        if (x not in C) and (y not in C):
            return False
    return True


def saveSolution(name, C):
    """save set C to file name as a VertexCover solution"""
    f = open(name, "w")
    s = ",".join([str(c) for c in C])
    f.write(s)
    f.close()


def loadCNF(name):
    """Load a graph in the DIMACS ascii format from
       the file "name" and return it as a pair (n, CNF),
       where n is the number of variables and CNF is the formula"""

    n = 0
    CNF = []

    f = open(name, "r")
    lines = f.readlines()
    for l in lines:
        s = l.split()
        if len(s) < 1:
            continue
        if s[0] == "c":
            continue
        elif s[0] == "p":
            n = int(s[2])
        else:
            C = [int(x) for x in s]
            CNF += [C[:-1]]

    f.close()
    return (n, CNF)


def saveCNF(name, cnf):
    """save formula cnf to the file name in DIMACS ascii format"""
    f = open(name, "w")
    nbvars = max([max(C) for C in cnf])
    nbclauses = len(cnf)

    # header
    f.write("p cnf %d %d\n" % (nbvars, nbclauses))

    # clauses
    for C in cnf:
        s = ""
        for x in C:
            s += str(x) + " "
        s += "0\n"
        f.write(s)

    f.close()
