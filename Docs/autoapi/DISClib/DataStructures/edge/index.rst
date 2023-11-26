:py:mod:`DISClib.DataStructures.edge`
=====================================

.. py:module:: DISClib.DataStructures.edge

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
   * Darío Correal



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   DISClib.DataStructures.edge.newEdge
   DISClib.DataStructures.edge.weight
   DISClib.DataStructures.edge.either
   DISClib.DataStructures.edge.other
   DISClib.DataStructures.edge.compareedges



.. py:function:: newEdge(va, vb, weight=0)

   Crea un nuevo arco entrelos vertices va y vb


.. py:function:: weight(edge)

   Retorna el peso de un arco


.. py:function:: either(edge)

   Retorna el vertice A del arco


.. py:function:: other(edge, veither)

   Retorna el vertice B del arco


.. py:function:: compareedges(edge1, edge2)

   Compara dos arcos y retorna True si son iguales


