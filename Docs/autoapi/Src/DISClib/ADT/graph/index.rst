:py:mod:`Src.DISClib.ADT.graph`
===============================

.. py:module:: Src.DISClib.ADT.graph

.. autoapi-nested-parse::

   # TODO cambiar comentarios de lincencia segun estandard del equipo
   * Copyright 2020, Departamento de sistemas y Computación,
   * Universidad de Los Andes
   *
   * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
   *
   *
   * This program is free software: you can redistribute it and/or modify
   * it under the terms of the GNU General Public License as published by
   * the Free Software Foundation, either version 3 of the License, or
   * (at your option) any later version.
   *
   * This program is distributed in the hope that it will be useful,
   * but WITHOUT ANY WARRANTY; without even the implied warranty of
   * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   * GNU General Public License for more details.
   *
   * You should have received a copy of the GNU General Public License
   * along with this program.  If not, see <http://www.gnu.org/licenses/>.
   *
   * Contribución de:
   *
   * Dario Correal
   *



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   Src.DISClib.ADT.graph.newGraph
   Src.DISClib.ADT.graph.insertVertex
   Src.DISClib.ADT.graph.removeVertex
   Src.DISClib.ADT.graph.numVertices
   Src.DISClib.ADT.graph.numEdges
   Src.DISClib.ADT.graph.vertices
   Src.DISClib.ADT.graph.edges
   Src.DISClib.ADT.graph.degree
   Src.DISClib.ADT.graph.outdegree
   Src.DISClib.ADT.graph.indegree
   Src.DISClib.ADT.graph.getEdge
   Src.DISClib.ADT.graph.addEdge
   Src.DISClib.ADT.graph.containsVertex
   Src.DISClib.ADT.graph.adjacents
   Src.DISClib.ADT.graph.adjacentEdges
   Src.DISClib.ADT.graph.graphSelector



Attributes
~~~~~~~~~~

.. autoapisummary::

   Src.DISClib.ADT.graph.switch_module


.. py:function:: newGraph(datastructure='ADJ_LIST', directed=False, size=10, cmpfunction=None)

   Crea un grafo vacio

   :param size: Tamaño inicial del grafo
   :param cmpfunction: Funcion de comparacion
   :param directed: Indica si el grafo es dirigido o no
   :param datastructure: Estructura de datos utilizada

   :returns: Un nuevo grafo vacío

   :raises Exception:


.. py:function:: insertVertex(graph, vertex)

   Inserta el vertice vertex en el grafo graph

   :param graph: El grafo sobre el que se ejecuta la operacion
   :param vertex: El vertice que se desea insertar

   :returns: El grafo graph con el nuevo vertice

   :raises Exception:


.. py:function:: removeVertex(graph, vertex)

   Remueve el vertice vertex del grafo graph

   :param graph: El grafo sobre el que se ejecuta la operacion
   :param vertex: El vertice que se desea remover

   :returns: El grafo sin el vertice vertex

   :raises Exception:


.. py:function:: numVertices(graph)

   Retorna el numero de vertices del  grafo graph

   :param graph: El grafo sobre el que se ejecuta la operacion

   :returns: El numero de vertices del grafo

   :raises Exception:


.. py:function:: numEdges(graph)

   Retorna el numero de arcos en el grafo graph

   :param graph: El grafo sobre el que se ejecuta la operacion

   :returns: El numero de vertices del grafo

   :raises Exception:


.. py:function:: vertices(graph)

   Retorna una lista con todos los vertices del grafo graph
   :param graph: El grafo sobre el que se ejecuta la operacion

   :returns: La lista con los vertices del grafo

   :raises Exception:


.. py:function:: edges(graph)

   Retorna una lista con todos los arcos del grafo graph

   :param graph: El grafo sobre el que se ejecuta la operacion

   :returns: Una lista con los arcos del grafo

   :raises Exception:


.. py:function:: degree(graph, vertex)

   Retorna el numero de arcos asociados al vertice vertex

   :param graph: El grafo sobre el que se ejecuta la operacion
   :param vertex: El vertice del que se desea conocer el grado

   :returns: El grado del vertice

   :raises Exception:


.. py:function:: outdegree(graph, vertex)

   Retorna el numero de arcos que salen del grafo vertex

   :param graph: El grafo sobre el que se ejecuta la operacion
   :param vertex: El vertice del que se desea conocer el grado

   :returns: El grado del vertice

   :raises Exception:


.. py:function:: indegree(graph, vertex)

   Retorna el numero de arcos que llegan al vertice vertex

   :param graph: El grafo sobre el que se ejecuta la operacion
   :param vertex: El vertice del que se desea conocer el grado

   :returns: El grado del vertice

   :raises Exception:


.. py:function:: getEdge(graph, vertexa, vertexb)

   Retorna el arco asociado a los vertices vertexa ---- vertexb

   :param graph: El grafo sobre el que se ejecuta la operacion
   :param vertexa: Vertice de inicio
   :param vertexb: Vertice destino

   :returns: El arco que une los verices vertexa y vertexb

   :raises Exception:


.. py:function:: addEdge(graph, vertexa, vertexb, weight=0)

   Agrega un arco entre los vertices vertexa ---- vertexb, con peso weight.
   Si el grafo es no dirigido se adiciona dos veces el mismo arco,
   en el mismo orden
   Si el grafo es dirigido se adiciona solo el arco vertexa --> vertexb

   :param graph: El grafo sobre el que se ejecuta la operacion
   :param vertexa: Vertice de inicio
   :param vertexb: Vertice de destino
   :param wight: peso del arco

   :returns: El grafo con el nuevo arco

   :raises Exception:


.. py:function:: containsVertex(graph, vertex)

   Retorna si el vertice vertex esta presente en el grafo

   :param graph: El grafo sobre el que se ejecuta la operacion
   :param vertex: Vertice que se busca

   :returns: True si el vertice esta presente

   :raises Exception:


.. py:function:: adjacents(graph, vertex)

   Retorna una lista con todos los vertices adyacentes al vertice vertex

   :param graph: El grafo sobre el que se ejecuta la operacion
   :param vertex: El vertice del que se quiere la lista

   :returns: La lista de adyacencias

   :raises Exception:


.. py:function:: adjacentEdges(graph, vertex)

   Retorna una lista con todos los arcos asociados a los vértices
   adyacentes de vertex

   :param graph: El grafo sobre el que se ejecuta la operacion
   :param vertex: El vertice del que se quiere la lista

   :returns: La lista de arcos adyacentes

   :raises Exception:


.. py:data:: switch_module

   

.. py:function:: graphSelector(datastructure)

   Carga dinamicamente el import de la estructura de datos
   seleccionada


