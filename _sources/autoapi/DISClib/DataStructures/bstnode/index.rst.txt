:py:mod:`DISClib.DataStructures.bstnode`
========================================

.. py:module:: DISClib.DataStructures.bstnode

.. autoapi-nested-parse::

   * Copyright 2020, Departamento de sistemas y Computación
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

   DISClib.DataStructures.bstnode.newNode
   DISClib.DataStructures.bstnode.getValue
   DISClib.DataStructures.bstnode.getKey



.. py:function:: newNode(key, value, size)

   Crea un nuevo nodo para un árbol binario y lo retorna
   :param value: El valor asociado a la llave
   :param key: la llave asociada a la pareja
   :param size: El tamaño del subarbol que cuelga de este nodo

   :returns: Un nodo con la pareja <llave, valor>

   :raises Exception:


.. py:function:: getValue(node)

   Retorna el valor asociado a una pareja llave valor
   :param node: El nodo con la pareja llave-valor

   :returns: El valor almacenado en el nodo

   :raises Exception:


.. py:function:: getKey(node)

   Retorna la llave asociado a una pareja llave valor
   :param node: El nodo con la pareja llave-valor

   :returns: La llave almacenada en el nodo

   :raises Exception:


