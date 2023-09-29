import pytest
import config
from DISClib.ADT import graph as g
from DISClib.ADT import stack
from DISClib.Algorithms.Graphs import dijsktra as djk
assert config


@pytest.fixture
def graph():
    graph = g.newGraph(size=7,
                       cmpfunction=compareVertices,
                       directed=True)

    g.insertVertex(graph, 'Bogota')
    g.insertVertex(graph, 'Duitama')
    g.insertVertex(graph, 'Armenia')
    g.insertVertex(graph, 'Honda')
    g.insertVertex(graph, 'Espinal')
    g.insertVertex(graph, 'Florencia')
    g.insertVertex(graph, 'Cali')

    g.addEdge(graph, 'Bogota', 'Duitama', 3.5)
    g.addEdge(graph, 'Bogota', 'Honda', 3)
    g.addEdge(graph, 'Bogota', 'Espinal', 4.5)
    g.addEdge(graph, 'Duitama', 'Armenia', 1)
    g.addEdge(graph, 'Honda', 'Duitama', 1)
    g.addEdge(graph, 'Honda', 'Espinal', 1)
    g.addEdge(graph, 'Honda', 'Armenia', 2.5)
    g.addEdge(graph, 'Honda', 'Florencia', 5.5)
    g.addEdge(graph, 'Espinal', 'Florencia', 2.4)
    g.addEdge(graph, 'Honda', 'Cali', 6)
    g.addEdge(graph, 'Florencia', 'Cali', 1)
    g.addEdge(graph, 'Armenia', 'Cali', 4)

    return graph


def test_dijkstra_bogota(graph):
    search = djk.Dijkstra(graph, 'Bogota')
    assert djk.hasPathTo(search, 'Cali') is True
    path = djk.pathTo(search, 'Cali')
    print('\n')
    while not stack.isEmpty(path):
        edge = stack.pop(path)
        print(edge['vertexA'] + "-->" +
              edge['vertexB'] +
              " costo: " +
              str(edge['weight']))
    print(str(djk.distTo(search, 'Cali')))


def test_dijkstra_cali(graph):
    search = djk.Dijkstra(graph, 'Cali')
    assert djk.hasPathTo(search, 'Bogota') is False


def test_dijkstra_honda(graph):
    search = djk.Dijkstra(graph, 'Honda')
    assert djk.hasPathTo(search, 'Cali') is True
    path = djk.pathTo(search, 'Cali')
    print('\n')
    while not stack.isEmpty(path):
        edge = stack.pop(path)
        print(edge['vertexA'] + "-->" +
              edge['vertexB'] +
              " costo: " +
              str(edge['weight']))
    print(str(djk.distTo(search, 'Cali')))


def test_dijkstra_armenia(graph):
    search = djk.Dijkstra(graph, 'Bogota')
    assert djk.hasPathTo(search, 'Armenia') is True
    path = djk.pathTo(search, 'Armenia')
    print('\n')
    while not stack.isEmpty(path):
        edge = stack.pop(path)
        print(edge['vertexA'] + "-->" +
              edge['vertexB'] +
              " costo: " +
              str(edge['weight']))
    print(str(djk.distTo(search, 'Armenia')))


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
