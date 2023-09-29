import pytest
import config
from DISClib.ADT import graph as g
from DISClib.ADT import stack
from DISClib.Algorithms.Graphs import dfo
assert config


@pytest.fixture
def graph():
    graph = g.newGraph(size=10, directed=True, cmpfunction=compareVertices)
    g.insertVertex(graph, 'Calculo1')
    g.insertVertex(graph, 'Calculo2')
    g.insertVertex(graph, 'Diseno1')
    g.insertVertex(graph, 'Diseno2')
    g.insertVertex(graph, 'Electiva')
    g.insertVertex(graph, 'Fisica1')
    g.insertVertex(graph, 'Ingles')
    g.insertVertex(graph, 'IP1')
    g.insertVertex(graph, 'IP2')
    g.insertVertex(graph, 'ProyectoFinal')

    g.addEdge(graph, 'Calculo1', 'Calculo2')
    g.addEdge(graph, 'Calculo2', 'IP2')
    g.addEdge(graph, 'Calculo2', 'Fisica1')
    g.addEdge(graph, 'Diseno1', 'Diseno2')
    g.addEdge(graph, 'Diseno2', 'ProyectoFinal')
    g.addEdge(graph, 'Electiva', 'ProyectoFinal')
    g.addEdge(graph, 'Fisica1', 'Diseno2')
    g.addEdge(graph, 'Ingles', 'ProyectoFinal')
    g.addEdge(graph, 'IP1', 'Diseno1')
    g.addEdge(graph, 'IP1', 'IP2')

    return graph


def test_dfo(graph):
    search = dfo.DepthFirstOrder(graph)
    assert stack.size(search['reversepost']) == 10
    print('')
    while not stack.isEmpty(search['reversepost']):
        top = stack.pop(search['reversepost'])
        print(top)


def compareVertices(searchname, element):
    if (searchname == element['key']):
        return 0
    elif (searchname < element['key']):
        return -1
    return 1
