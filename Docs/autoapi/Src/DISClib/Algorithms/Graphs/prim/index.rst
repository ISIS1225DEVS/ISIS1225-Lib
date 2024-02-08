:py:mod:`Src.DISClib.Algorithms.Graphs.prim`
============================================

.. py:module:: Src.DISClib.Algorithms.Graphs.prim

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

   Src.DISClib.Algorithms.Graphs.prim.PrimMST
   Src.DISClib.Algorithms.Graphs.prim.prim
   Src.DISClib.Algorithms.Graphs.prim.scan
   Src.DISClib.Algorithms.Graphs.prim.edgesMST
   Src.DISClib.Algorithms.Graphs.prim.weightMST
   Src.DISClib.Algorithms.Graphs.prim.initSearch



.. py:function:: PrimMST(graph, origin=None)

   Implementa el algoritmo de Prim
   :param graph: El grafo de busqueda

   :returns: La estructura search con los MST

   :raises Exception:


.. py:function:: prim(graph, search, v)

   :param search: La estructura de busqueda
   :param v: Vertice desde donde se relajan los pesos

   :returns: El grafo con los arcos relajados

   :raises Exception:


.. py:function:: scan(graph, search, vertex)

   :param search: La estructura de busqueda
   :param vertex: El vertice destino

   :returns: El costo total para llegar de source a
             vertex. Infinito si no existe camino

   :raises Exception:


.. py:function:: edgesMST(graph, search)

   :param search: La estructura de busqueda
   :param vertex: El vertice de destino

   :returns: Una pila con el camino entre source y vertex

   :raises Exception:


.. py:function:: weightMST(graph, search)


.. py:function:: initSearch(graph)

   Inicializa la estructura de busqueda y deja
   todos los arcos en infinito.
   Se inserta en la cola el vertice source
   :param graph: El grafo a examinar
   :param source: El vertice fuente

   :returns: Estructura de busqueda inicializada

   :raises Exception:


