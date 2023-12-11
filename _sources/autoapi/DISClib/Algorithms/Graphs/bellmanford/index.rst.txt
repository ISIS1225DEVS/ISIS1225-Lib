:py:mod:`DISClib.Algorithms.Graphs.bellmanford`
===============================================

.. py:module:: DISClib.Algorithms.Graphs.bellmanford

.. autoapi-nested-parse::

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

   DISClib.Algorithms.Graphs.bellmanford.BellmanFord
   DISClib.Algorithms.Graphs.bellmanford.relax
   DISClib.Algorithms.Graphs.bellmanford.distTo
   DISClib.Algorithms.Graphs.bellmanford.hasPathTo
   DISClib.Algorithms.Graphs.bellmanford.pathTo
   DISClib.Algorithms.Graphs.bellmanford.findNegativeCycle
   DISClib.Algorithms.Graphs.bellmanford.hasNegativecycle
   DISClib.Algorithms.Graphs.bellmanford.initSearch



.. py:function:: BellmanFord(graph, source)

   Implementa el algoritmo de Bellman-Ford
   :param graph: El grafo de busqueda
   :param source: El vertice de inicio

   :returns: La estructura search con los caminos de peso mínimos

   :raises Exception:


.. py:function:: relax(graph, search, v)

   Relaja el peso de los arcos del grafo
   :param search: La estructura de busqueda
   :param v: Vertice desde donde se relajan los pesos

   :returns: El grafo con los arcos relajados

   :raises Exception:


.. py:function:: distTo(search, vertex)

   Retorna el costo para llegar del vertice
   source al vertice vertex.
   :param search: La estructura de busqueda
   :param vertex: El vertice destino

   :returns: El costo total para llegar de source a
             vertex. Infinito si no existe camino

   :raises Exception:


.. py:function:: hasPathTo(search, vertex)

   Indica si hay camino entre source
   y vertex
   :param search: La estructura de busqueda
   :param vertex: El vertice de destino

   :returns: True si existe camino

   :raises Exception:


.. py:function:: pathTo(search, vertex)

   Retorna el camino entre source y vertex
   en una pila.
   :param search: La estructura de busqueda
   :param vertex: El vertice de destino

   :returns: Una pila con el camino entre source y vertex

   :raises Exception:


.. py:function:: findNegativeCycle(graph, search)

   Identifica ciclos negativos en el grafo


.. py:function:: hasNegativecycle(search)


.. py:function:: initSearch(graph, source)

   Inicializa la estructura de busqueda y deja
   todos los arcos en infinito.
   Se inserta en la cola el vertice source
   :param graph: El grafo a examinar
   :param source: El vertice fuente

   :returns: Estructura de busqueda inicializada

   :raises Exception:


