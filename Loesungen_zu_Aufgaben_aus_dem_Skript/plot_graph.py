import networkx as nx
from matplotlib import pylab


def main():
    graph = nx.Graph({'A': ['A', 'B', 'C'], 'B': ['C'], 'C': ['D'], 'D': ['A']})
    nx.draw(graph)
    pylab.show()
