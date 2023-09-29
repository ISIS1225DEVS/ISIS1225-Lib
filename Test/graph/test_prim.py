import pytest
import config
from DISClib.ADT import graph as g
from DISClib.ADT import queue as q
from DISClib.Algorithms.Graphs import prim
assert config


@pytest.fixture
def graph():
    graph = g.newGraph(size=7,
                       cmpfunction=compareVertices,
                       directed=False)

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
    g.addEdge(graph, 'Duitama', 'Armenia', 2)
    g.addEdge(graph, 'Honda', 'Duitama', 1)
    g.addEdge(graph, 'Honda', 'Espinal', 1.5)
    g.addEdge(graph, 'Honda', 'Armenia', 2.5)
    g.addEdge(graph, 'Honda', 'Florencia', 5.5)
    g.addEdge(graph, 'Espinal', 'Florencia', 6.5)
    g.addEdge(graph, 'Honda', 'Cali', 6)
    g.addEdge(graph, 'Florencia', 'Cali', 5)
    g.addEdge(graph, 'Armenia', 'Cali', 4)

    return graph


@pytest.fixture
def graph2():
    graph = g.newGraph(size=8,
                       cmpfunction=compareVertices,
                       directed=False)

    g.insertVertex(graph, 'Bogota')
    g.insertVertex(graph, 'Duitama')
    g.insertVertex(graph, 'Armenia')
    g.insertVertex(graph, 'Honda')
    g.insertVertex(graph, 'Espinal')
    g.insertVertex(graph, 'Florencia')
    g.insertVertex(graph, 'Cali')
    g.insertVertex(graph, 'Medellin')

    g.addEdge(graph, 'Bogota', 'Duitama', 5)
    g.addEdge(graph, 'Bogota', 'Armenia', 8)
    g.addEdge(graph, 'Duitama', 'Armenia', 2)
    g.addEdge(graph, 'Armenia', 'Honda', 2)
    g.addEdge(graph, 'Espinal', 'Cali', 7)
    g.addEdge(graph, 'Cali', 'Medellin', 1)
    g.addEdge(graph, 'Espinal', 'Florencia', 2)
    g.addEdge(graph, 'Florencia', 'Medellin', 15)
    g.addEdge(graph, 'Honda', 'Medellin', 6)
    g.addEdge(graph, 'Duitama', 'Espinal', 9)
    return graph


@pytest.fixture
def graph3():
    graph = g.newGraph(size=8,
                       cmpfunction=compareVertices,
                       directed=False)

    g.insertVertex(graph, 'Bogota')
    g.insertVertex(graph, 'Duitama')
    g.insertVertex(graph, 'Armenia')
    g.insertVertex(graph, 'Honda')
    g.insertVertex(graph, 'Espinal')
    g.insertVertex(graph, 'Florencia')
    g.insertVertex(graph, 'Cali')
    g.insertVertex(graph, 'Medellin')

    g.addEdge(graph, 'Bogota', 'Duitama', 5)
    g.addEdge(graph, 'Bogota', 'Armenia', 8)
    g.addEdge(graph, 'Duitama', 'Armenia', 2)
    g.addEdge(graph, 'Armenia', 'Honda', 2)
    g.addEdge(graph, 'Espinal', 'Cali', 7)
    g.addEdge(graph, 'Cali', 'Medellin', 1)
    g.addEdge(graph, 'Espinal', 'Florencia', 2)
    g.addEdge(graph, 'Florencia', 'Medellin', 15)
    return graph


def test_prim(graph):
    print("Test1")
    search = prim.PrimMST(graph)
    weight = prim.weightMST(graph, search)
    print('\n')
    path = search['mst']
    while not q.isEmpty(path):
        edge = q.dequeue(path)
        print(edge['vertexA'] + "-->" +
              edge['vertexB'] +
              " costo: " +
              str(edge['weight']))
    print(str(weight))


def test_prim2(graph2):
    print("Test2")
    search = prim.PrimMST(graph2)
    weight = prim.weightMST(graph2, search)
    print('\n')
    path = search['mst']
    while not q.isEmpty(path):
        edge = q.dequeue(path)
        print(edge['vertexA'] + "-->" +
              edge['vertexB'] +
              " costo: " +
              str(edge['weight']))
    print(str(weight))


def test_prim3(graph3):
    print("Test3")
    search = prim.PrimMST(graph3)
    weight = prim.weightMST(graph3, search)
    print('\n')
    path = search['mst']
    while not q.isEmpty(path):
        edge = q.dequeue(path)
        print(edge['vertexA'] + "-->" +
              edge['vertexB'] +
              " costo: " +
              str(edge['weight']))
    print(str(weight))


def test_prim4(graph2):
    print("Test4")
    search = prim.PrimMST(graph2, 'Armenia')
    weight = prim.weightMST(graph2, search)
    print('\n')
    path = search['mst']
    while not q.isEmpty(path):
        edge = q.dequeue(path)
        print(edge['vertexA'] + "-->" +
              edge['vertexB'] +
              " costo: " +
              str(edge['weight']))
    print(str(weight))


def test_prim5(graph3):
    print("Test5")
    search = prim.PrimMST(graph3, 'Bogota')
    weight = prim.weightMST(graph3, search)
    print('\n')
    path = search['mst']
    while not q.isEmpty(path):
        edge = q.dequeue(path)
        print(edge['vertexA'] + "-->" +
              edge['vertexB'] +
              " costo: " +
              str(edge['weight']))
    print(str(weight))


def test_prim6(graph):
    print("Test6")
    search = prim.PrimMST(graph, 'Bogota')
    weight = prim.weightMST(graph, search)
    print('\n')
    path = search['mst']
    while not q.isEmpty(path):
        edge = q.dequeue(path)
        print(edge['vertexA'] + "-->" +
              edge['vertexB'] +
              " costo: " +
              str(edge['weight']))
    print(str(weight))


def compareVertices(searchname, element):
    if (searchname == element['key']):
        return 0
    elif (searchname < element['key']):
        return -1
    return 1
