import pytest
import config
from DISClib.ADT import graph as g
from DISClib.Algorithms.Graphs import scc
assert config


@pytest.fixture
def graph():
    graph = g.newGraph(size=12, directed=True, cmpfunction=compareVertices)

    g.insertVertex(graph, 'A1')
    g.insertVertex(graph, 'A2')
    g.insertVertex(graph, 'A3')
    g.insertVertex(graph, 'A4')
    g.insertVertex(graph, 'B1')
    g.insertVertex(graph, 'B2')
    g.insertVertex(graph, 'B3')
    g.insertVertex(graph, 'C1')
    g.insertVertex(graph, 'C2')
    g.insertVertex(graph, 'C3')
    g.insertVertex(graph, 'C4')
    g.insertVertex(graph, 'C5')

    g.addEdge(graph, 'A1', 'A2')
    g.addEdge(graph, 'A2', 'A3')
    g.addEdge(graph, 'A3', 'A2')
    g.addEdge(graph, 'A2', 'A1')
    g.addEdge(graph, 'A3', 'A4')
    g.addEdge(graph, 'A4', 'A3')

    g.addEdge(graph, 'C1', 'C5')
    g.addEdge(graph, 'C1', 'C2')
    g.addEdge(graph, 'C2', 'C3')
    g.addEdge(graph, 'C5', 'C2')
    g.addEdge(graph, 'C3', 'C4')
    g.addEdge(graph, 'C4', 'C1')

    g.addEdge(graph, 'B1', 'B2')
    g.addEdge(graph, 'B2', 'B3')
    g.addEdge(graph, 'B3', 'B1')
    g.addEdge(graph, 'B2', 'B1')

    g.addEdge(graph, 'A2', 'C1')
    g.addEdge(graph, 'C3', 'A4')

    g.addEdge(graph, 'C5', 'B2')
    g.addEdge(graph, 'B3', 'C2')

    return graph


def test_scc(graph):
    sc = scc.KosarajuSCC(graph)
    assert scc.connectedComponents(sc) == 1
    assert scc.stronglyConnected(sc, 'A1', 'A4') is True
    assert scc.stronglyConnected(sc, 'A1', 'B3') is True


# --------------------------------------
#       Funciones de Comparacion
# --------------------------------------


def compareVertices(searchname, element):
    if (searchname == element['key']):
        return 0
    elif (searchname < element['key']):
        return -1
    return 1
