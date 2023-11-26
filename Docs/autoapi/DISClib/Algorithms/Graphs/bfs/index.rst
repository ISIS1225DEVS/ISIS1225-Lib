:py:mod:`DISClib.Algorithms.Graphs.bfs`
=======================================

.. py:module:: DISClib.Algorithms.Graphs.bfs

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

   DISClib.Algorithms.Graphs.bfs.BreadhtFisrtSearch
   DISClib.Algorithms.Graphs.bfs.bfsVertex
   DISClib.Algorithms.Graphs.bfs.hasPathTo
   DISClib.Algorithms.Graphs.bfs.pathTo



.. py:function:: BreadhtFisrtSearch(graph, source)

   Genera un recorrido BFS sobre el grafo graph
   :param graph: El grafo a recorrer
   :param source: Vertice de inicio del recorrido.

   :returns: Una estructura para determinar los vertices
             conectados a source

   :raises Exception:


.. py:function:: bfsVertex(search, graph, source)

   Funcion auxiliar para calcular un recorrido BFS
   :param search: Estructura para almacenar el recorrido
   :param vertex: Vertice de inicio del recorrido.

   :returns: Una estructura para determinar los vertices
             conectados a source

   :raises Exception:


.. py:function:: hasPathTo(search, vertex)

   Indica si existe un camino entre el vertice source
   y el vertice vertex
   :param search: Estructura de recorrido BFS
   :param vertex: Vertice destino

   :returns: True si existe un camino entre source y vertex

   :raises Exception:


.. py:function:: pathTo(search, vertex)

   Retorna el camino entre el vertices source y el
   vertice vertex
   :param search: La estructura con el recorrido
   :param vertex: Vertice de destingo

   :returns: Una pila con el camino entre el vertices source y el
             vertice vertex

   :raises Exception:


