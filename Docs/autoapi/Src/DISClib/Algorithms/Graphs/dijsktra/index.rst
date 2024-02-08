:py:mod:`Src.DISClib.Algorithms.Graphs.dijsktra`
================================================

.. py:module:: Src.DISClib.Algorithms.Graphs.dijsktra

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

   Src.DISClib.Algorithms.Graphs.dijsktra.Dijkstra
   Src.DISClib.Algorithms.Graphs.dijsktra.relax
   Src.DISClib.Algorithms.Graphs.dijsktra.distTo
   Src.DISClib.Algorithms.Graphs.dijsktra.hasPathTo
   Src.DISClib.Algorithms.Graphs.dijsktra.pathTo
   Src.DISClib.Algorithms.Graphs.dijsktra.initSearch



.. py:function:: Dijkstra(graph, source)

   Implementa el algoritmo de Dijkstra
   :param graph: El grafo de busqueda
   :param source: El vertice de inicio

   :returns: Un nuevo grafo vacío

   :raises Exception:


.. py:function:: relax(search, edge)

   Relaja el peso de los arcos del grafo con la
   nueva de un nuevo arco
   :param search: La estructura de busqueda
   :param edge: El nuevo arco

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


.. py:function:: initSearch(graph, source)

   Inicializa la estructura de busqueda y deja
   todos los arcos en infinito.
   Se inserta en la cola indexada el vertice source
   :param graph: El grafo a examinar
   :param source: El vertice fuente

   :returns: Estructura de busqueda inicializada

   :raises Exception:


