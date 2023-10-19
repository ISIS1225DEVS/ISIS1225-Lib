:py:mod:`DISClib.Algorithms.Sorting.quicksort`
==============================================

.. py:module:: DISClib.Algorithms.Sorting.quicksort

.. autoapi-nested-parse::

   * Copyright 2020, Departamento de sistemas y Computación,
   * Universidad de Los Andes
   *
   *
   * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
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

   DISClib.Algorithms.Sorting.quicksort.partition
   DISClib.Algorithms.Sorting.quicksort.quicksort
   DISClib.Algorithms.Sorting.quicksort.sort



.. py:function:: partition(lst, lo, hi, sort_crit)

   Función que va dejando el pivot en su lugar, mientras mueve
   elementos menores a la izquierda del pivot y elementos mayores a
   la derecha del pivot


.. py:function:: quicksort(lst, lo, hi, sort_crit)

   Se localiza el pivot, utilizando la funcion de particion.
   Luego se hace la recursión con los elementos a la izquierda del pivot
   y los elementos a la derecha del pivot


.. py:function:: sort(lst, sort_crit)


