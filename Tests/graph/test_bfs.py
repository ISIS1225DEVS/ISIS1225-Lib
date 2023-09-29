import pytest
import config
from DISClib.DataStructures import edge as e
from DISClib.ADT import graph as g
from DISClib.ADT import stack as stk
from DISClib.Algorithms.Graphs import bfs
assert config


@pytest.fixture
def graph():
    graph = g.newGraph(size=10, cmpfunction=compareVertices)
    g.insertVertex(graph, 'Bogota')
    g.insertVertex(graph, 'Yopal')
    g.insertVertex(graph, 'Cali')
    g.insertVertex(graph, 'Medellin')
    g.insertVertex(graph, 'Pasto')
    g.insertVertex(graph, 'Barranquilla')
    g.insertVertex(graph, 'Manizales')

    g.addEdge(graph, 'Bogota', 'Yopal')
    g.addEdge(graph, 'Bogota', 'Medellin')
    g.addEdge(graph, 'Bogota', 'Pasto')
    g.addEdge(graph, 'Bogota', 'Cali')
    g.addEdge(graph, 'Yopal', 'Medellin')
    g.addEdge(graph, 'Medellin', 'Pasto')
    g.addEdge(graph, 'Cali', 'Pasto')
    g.addEdge(graph, 'Cali', 'Barranquilla')
    g.addEdge(graph, 'Barranquilla', 'Manizales')
    g.addEdge(graph, 'Pasto', 'Manizales')

    return graph


@pytest.fixture
def digraph():
    digraph = g.newGraph(size=10, directed=True,
                         cmpfunction=compareVertices)
    return digraph


def test_edgeMethods(graph):
    edge = e.newEdge('Bogota', 'Cali')
    assert 'Bogota' == e.either(edge)
    assert 'Cali' == e.other(edge, 'Bogota')
    assert e.weight(edge) == 0


def test_insertEdges(graph):
    assert g.numVertices(graph) == 7
    assert g.numEdges(graph) == 10


def test_dfs(graph):
    search = bfs.BreadhtFisrtSearch(graph, 'Yopal')
    assert bfs.hasPathTo(search, 'Manizales') is True
    path = bfs.pathTo(search, 'Manizales')
    assert stk.size(path) == 4

# --------------------------------------
#       Funciones de Comparacion
# --------------------------------------


def compareVertices(searchname, element):
    if (searchname == element['key']):
        return 0
    elif (searchname < element['key']):
        return -1
    return 1
