import pytest
import config
from DISClib.ADT import graph as g
from DISClib.ADT import stack
from DISClib.Algorithms.Graphs import bellmanford as bf
assert config


@pytest.fixture
def graph():
    graph = g.newGraph(size=7,
                       cmpfunction=compareVertices,
                       directed=True)

    g.insertVertex(graph, 'S1')
    g.insertVertex(graph, 'S2')
    g.insertVertex(graph, 'S3')
    g.insertVertex(graph, 'S4')
    g.insertVertex(graph, 'S5')
    g.insertVertex(graph, 'S6')
    g.insertVertex(graph, 'S7')

    g.addEdge(graph, 'S1', 'S2', 9)
    g.addEdge(graph, 'S1', 'S3', 22)
    g.addEdge(graph, 'S2', 'S7', -3)
    g.addEdge(graph, 'S3', 'S2', 5)
    g.addEdge(graph, 'S3', 'S7', 3)
    g.addEdge(graph, 'S3', 'S4', -1)
    g.addEdge(graph, 'S3', 'S6', 6)
    g.addEdge(graph, 'S3', 'S5', 5.5)
    g.addEdge(graph, 'S4', 'S1', 1.5)
    g.addEdge(graph, 'S4', 'S5', 0.4)
    g.addEdge(graph, 'S5', 'S6', -8)
    g.addEdge(graph, 'S7', 'S6', 10)
    return graph


@pytest.fixture
def acgraph():
    graph = g.newGraph(size=7,
                       cmpfunction=compareVertices,
                       directed=True)

    g.insertVertex(graph, 'S1')
    g.insertVertex(graph, 'S2')
    g.insertVertex(graph, 'S3')
    g.insertVertex(graph, 'S4')
    g.insertVertex(graph, 'S5')
    g.insertVertex(graph, 'S6')
    g.insertVertex(graph, 'S7')

    g.addEdge(graph, 'S1', 'S2', 9)
    g.addEdge(graph, 'S1', 'S3', 22)
    g.addEdge(graph, 'S2', 'S7', -3)
    g.addEdge(graph, 'S3', 'S2', 5)
    g.addEdge(graph, 'S3', 'S7', 3)
    g.addEdge(graph, 'S3', 'S4', -1)
    g.addEdge(graph, 'S3', 'S6', 6)
    g.addEdge(graph, 'S3', 'S5', 5.5)
    g.addEdge(graph, 'S1', 'S4', 1.5)
    g.addEdge(graph, 'S4', 'S5', 0.4)
    g.addEdge(graph, 'S5', 'S6', -8)
    g.addEdge(graph, 'S7', 'S6', 10)
    return graph


def test_bellman_ciclo_bogota(graph):
    search = bf.BellmanFord(graph, 'S1')
    assert bf.hasPathTo(search, 'S6') is True
    path = bf.pathTo(search, 'S6')
    print('\n')
    while not stack.isEmpty(path):
        edge = stack.pop(path)
        print(edge['vertexA'] + "-->" +
              edge['vertexB'] +
              " costo: " +
              str(edge['weight']))
    print(str(bf.distTo(search, 'S6')))


def test_bellman_bogotaac(acgraph):
    search = bf.BellmanFord(acgraph, 'S1')
    assert bf.hasPathTo(search, 'S6') is True
    path = bf.pathTo(search, 'S6')
    print('\n')
    while not stack.isEmpty(path):
        edge = stack.pop(path)
        print(edge['vertexA'] + "-->" +
              edge['vertexB'] +
              " costo: " +
              str(edge['weight']))
    print(str(bf.distTo(search, 'S6')))


def comparekeys(key, element):
    if (key is not None and element is not None):
        if (key == element['key']):
            return True
    return False


def compareVertices(searchname, element):
    if (searchname == element['key']):
        return 0
    elif (searchname < element['key']):
        return -1
    return 1
