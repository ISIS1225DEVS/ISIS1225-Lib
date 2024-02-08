:py:mod:`Src.DISClib.Algorithms.Graphs.dfo`
===========================================

.. py:module:: Src.DISClib.Algorithms.Graphs.dfo

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

   Src.DISClib.Algorithms.Graphs.dfo.DepthFirstOrder
   Src.DISClib.Algorithms.Graphs.dfo.dfsVertex
   Src.DISClib.Algorithms.Graphs.dfo.comparenames



.. py:function:: DepthFirstOrder(graph)


.. py:function:: dfsVertex(graph, search, vertex)

   Genera un recorrido DFS sobre el grafo graph
   :param graph: El grafo a recorrer
   :param source: Vertice de inicio del recorrido.

   :returns: Una estructura para determinar los vertices
             conectados a source

   :raises Exception:


.. py:function:: comparenames(self, searchname, element)


