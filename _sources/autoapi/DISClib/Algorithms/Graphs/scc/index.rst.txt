:py:mod:`DISClib.Algorithms.Graphs.scc`
=======================================

.. py:module:: DISClib.Algorithms.Graphs.scc

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

   DISClib.Algorithms.Graphs.scc.KosarajuSCC
   DISClib.Algorithms.Graphs.scc.sccCount
   DISClib.Algorithms.Graphs.scc.stronglyConnected
   DISClib.Algorithms.Graphs.scc.connectedComponents
   DISClib.Algorithms.Graphs.scc.reverseGraph
   DISClib.Algorithms.Graphs.scc.comparenames



.. py:function:: KosarajuSCC(graph)

   Implementa el algoritmo de Kosaraju
   para encontrar los componentes conectados
   de un grafo dirigido
   :param graph: El grafo a examinar

   :returns: Una estructura con los componentes
             conectados

   :raises Exception:


.. py:function:: sccCount(graph, scc, vert)

   Este algoritmo cuenta el número de componentes conectados.
   Deja en idscc, el número del componente al que pertenece cada vértice


.. py:function:: stronglyConnected(scc, verta, vertb)

   Dados dos vértices, informa si están fuertemente conectados o no.


.. py:function:: connectedComponents(scc)

   Retorna el numero de componentes conectados


.. py:function:: reverseGraph(graph)

   Retornar el reverso del grafo graph


.. py:function:: comparenames(searchname, element)


