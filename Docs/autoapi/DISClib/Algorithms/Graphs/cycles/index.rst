:py:mod:`DISClib.Algorithms.Graphs.cycles`
==========================================

.. py:module:: DISClib.Algorithms.Graphs.cycles

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

   DISClib.Algorithms.Graphs.cycles.DirectedCycle
   DISClib.Algorithms.Graphs.cycles.dfs
   DISClib.Algorithms.Graphs.cycles.hasCycle
   DISClib.Algorithms.Graphs.cycles.cycle
   DISClib.Algorithms.Graphs.cycles.initStructures



.. py:function:: DirectedCycle(graph)

   Detecta ciclos en un grafo dirigido
   :param graph: El grafo de busqueda

   :returns: El ciclo si existe

   :raises Exception:


.. py:function:: dfs(graph, search, v)

   DFS
   :param search: La estructura de busqueda
   :param v: Vertice desde donde se relajan los pesos

   :returns: El grafo

   :raises Exception:


.. py:function:: hasCycle(search)


.. py:function:: cycle(search)


.. py:function:: initStructures(graph)

   :param graph: El grafo a examinar
   :param source: El vertice fuente

   :returns: Estructura de busqueda inicializada

   :raises Exception:


