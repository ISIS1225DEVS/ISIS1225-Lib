import pytest
import config
from DISClib.DataStructures import edge as e
from DISClib.ADT import graph as g
assert config


@pytest.fixture
def graph():
    graph = g.newGraph(size=10, directed=False, cmpfunction=comparenames)
    return graph


@pytest.fixture
def digraph():
    digraph = g.newGraph(size=10, directed=True,
                         cmpfunction=comparenames)
    return digraph


def test_edgeMethods(graph):
    edge = e.newEdge('Bogota', 'Cali')
    assert 'Bogota' == e.either(edge)
    assert 'Cali' == e.other(edge, 'Bogota')
    assert e.weight(edge) == 0


def test_insertVertex(graph):
    g.insertVertex(graph, 'Bogota')
    g.insertVertex(graph, 'Yopal')
    g.insertVertex(graph, 'Cali')
    g.insertVertex(graph, 'Medellin')
    g.insertVertex(graph, 'Pasto')
    g.insertVertex(graph, 'Barranquilla')
    g.insertVertex(graph, 'Manizales')
    assert g.numVertices(graph) == 7


def test_insertEdges(graph):
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
    assert g.numVertices(graph) == 7
    assert g.numEdges(graph) == 10


def test_getEdgesDigraph(digraph):
    g.insertVertex(digraph, 'Bogota')
    g.insertVertex(digraph, 'Yopal')
    g.insertVertex(digraph, 'Cali')
    g.insertVertex(digraph, 'Medellin')
    g.insertVertex(digraph, 'Pasto')
    g.insertVertex(digraph, 'Barranquilla')
    g.insertVertex(digraph, 'Manizales')
    g.addEdge(digraph, 'Bogota', 'Yopal', 2)
    g.addEdge(digraph, 'Bogota', 'Medellin', 3)
    g.addEdge(digraph, 'Bogota', 'Pasto', 1)
    g.addEdge(digraph, 'Bogota', 'Cali', 10)
    g.addEdge(digraph, 'Yopal', 'Medellin', 20)
    g.addEdge(digraph, 'Medellin', 'Pasto', 4)
    g.addEdge(digraph, 'Cali', 'Pasto', 6)
    g.addEdge(digraph, 'Cali', 'Barranquilla', 3)
    g.addEdge(digraph, 'Barranquilla', 'Manizales', 10)
    g.addEdge(digraph, 'Pasto', 'Manizales', 8)
    assert g.numVertices(digraph) == 7
    assert g.numEdges(digraph) == 10
    edge = g.getEdge(digraph, 'Medellin', 'Pasto')
    assert edge['weight'] == 4


def test_getEdgesGraph(graph):
    g.insertVertex(graph, 'Bogota')
    g.insertVertex(graph, 'Yopal')
    g.insertVertex(graph, 'Cali')
    g.insertVertex(graph, 'Medellin')
    g.insertVertex(graph, 'Pasto')
    g.insertVertex(graph, 'Barranquilla')
    g.insertVertex(graph, 'Manizales')
    g.addEdge(graph, 'Bogota', 'Yopal', 2)
    g.addEdge(graph, 'Bogota', 'Medellin', 3)
    g.addEdge(graph, 'Bogota', 'Pasto', 1)
    g.addEdge(graph, 'Bogota', 'Cali', 10)
    g.addEdge(graph, 'Yopal', 'Medellin', 20)
    g.addEdge(graph, 'Medellin', 'Pasto', 4)
    g.addEdge(graph, 'Cali', 'Pasto', 6)
    g.addEdge(graph, 'Cali', 'Barranquilla', 3)
    g.addEdge(graph, 'Barranquilla', 'Manizales', 10)
    g.addEdge(graph, 'Pasto', 'Manizales', 8)
    assert g.numVertices(graph) == 7
    assert g.numEdges(graph) == 10
    edge = g.getEdge(graph, 'Pasto', 'Medellin')
    assert edge['weight'] == 4


def comparenames(searchname, element):
    if (searchname == element['key']):
        return 0
    elif (searchname < element['key']):
        return -1
    return 1


def comparelst(self, searchname, element):
    return (searchname == element)


def test_newEdge():
    edge = e.newEdge(1, 1, 1)
    assert edge is not None
